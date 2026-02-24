#!/bin/sh


	set -e
	echo "$EXAMPLE_LINC"
	echo "target_dir: $TARGET"
	echo "Start Processing"

	curl --fail \
	     --silent \
	     --show-error \
	     --location \
	     --url "$EXAMPLE_LINC" \
	     --output "$TARGET/output.html"


	echo "Process Finished"