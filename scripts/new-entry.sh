#!/bin/sh
# Scaffold a new build log entry and its image folder.
# Usage: scripts/new-entry.sh "fitting the bulkheads"
set -eu

if [ $# -lt 1 ]; then
  echo "usage: $0 \"short title\"" >&2
  exit 1
fi

root=$(cd "$(dirname "$0")/.." && pwd)
title=$*
slug=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]' | tr -cs '[:alnum:]' '-' | sed 's/^-//;s/-$//')

last=$(ls "$root/build_log" | sed -n 's/^\([0-9][0-9][0-9]\)-.*\.md$/\1/p' | sort -n | tail -1)
# 10# forces base 10: under /bin/sh a bare 017 is octal (=15) and 008/009 are a fatal
# "value too great for base" error.
next=$(printf '%03d' $(( 10#${last:-0} + 1 )))

entry="$root/build_log/$next-$slug.md"
imgdir="$root/build_log/images/$next-$slug"

if [ -e "$entry" ]; then
  echo "$entry already exists" >&2
  exit 1
fi

prev=$(ls "$root/build_log" | sed -n 's/^\([0-9][0-9][0-9]-.*\)\.md$/\1/p' | sort | tail -1)
if [ -n "${prev:-}" ]; then
  prevlink="[← Previous entry]($prev.md)"
else
  prevlink="← Previous entry  *(none)*"
fi

# Strip the template's leading HTML comment, then substitute the placeholders.
sed -e '1,/^-->$/d' \
    -e "s/NNN-short-slug/$next-$slug/g" \
    -e "s/NNN · Short imperative title/$next · $title/" \
    -e "s|\[← Previous entry\](000-previous.md)|$prevlink|g" \
    -e "s|\[Next entry →\](000-next.md)|Next entry →  *(not yet written)*|g" \
    -e "s/^| \*\*Date\*\* | YYYY-MM-DD |/| **Date** | $(date +%Y-%m-%d) |/" \
    "$root/build_log/_template.md" | sed '/./,$!d' > "$entry"

mkdir -p "$imgdir"
touch "$imgdir/.gitkeep"

echo "created $entry"
echo "created $imgdir/"
echo
echo "Next:"
echo "  1. write the entry"
echo "  2. add a row to build_log/README.md"
echo "  3. update the phase table in README.md"
echo "  4. fix the 'Next entry ->' link at the top and bottom of build_log/$prev.md"
