#!/bin/bash

# Define the old and new Firebase project IDs
OLD_PROJECT="sattal-a27f2"
NEW_PROJECT="sattal-a27f2"

echo "Searching for instances of '$OLD_PROJECT' and replacing with '$NEW_PROJECT'..."

# Find and update files, excluding the .git directory to keep your git history safe
find . -type f -not -path '*/.git/*' | while read -r file; do
    # Check if the file contains the old project ID before running sed
    if grep -q "$OLD_PROJECT" "$file"; then
        echo "Updating: $file"
        
        # Adjust sed syntax based on OS (macOS/BSD vs Linux)
        if [[ "$OSTYPE" == "darwin"* ]]; then
            sed -i '' "s/$OLD_PROJECT/$NEW_PROJECT/g" "$file"
        else
            sed -i "s/$OLD_PROJECT/$NEW_PROJECT/g" "$file"
        fi
    fi
done

echo "Done! Run 'git diff' to review the changes before committing."
