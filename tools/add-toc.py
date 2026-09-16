#!/usr/bin/env python3
"""Add Table of Contents to multi-section markdown files."""

import re
import sys
from pathlib import Path


def slugify(text):
    """Convert heading text to a GitHub-style anchor slug."""
    slug = text.strip().lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug


def extract_headings(content):
    """Extract all ## headings from markdown content."""
    return re.findall(r'^(##+)\s+(.+)$', content, re.MULTILINE)


def generate_toc(headings):
    """Generate a markdown TOC from headings."""
    lines = ['\n', '<!-- TOC -->', '<details><summary>Table of Contents</summary>', '']
    for level, text in headings:
        indent = '  ' * (len(level) - 1)  # ## = 1 indent, ### = 2, etc.
        slug = slugify(text)
        lines.append(f'{indent}- [{text}](#{slug})')
    lines.append('')
    lines.append('</details>')
    lines.append('')
    return '\n'.join(lines)


def add_toc_to_file(filepath):
    """Add TOC to a markdown file if it has 2+ ## headings."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if already has TOC
    if '<!-- TOC -->' in content:
        return False

    headings = extract_headings(content)
    if len(headings) < 2:
        return False

    toc = generate_toc(headings)

    # Find insertion point: after the first H1 title, before first ## heading
    # Handle YAML frontmatter
    frontmatter_match = re.match(r'^---\n.*?^---\n', content, re.MULTILINE | re.DOTALL)
    frontmatter_end = frontmatter_match.end() if frontmatter_match else 0
    
    # Find the H1 title (after frontmatter if present)
    title_pattern = r'^#\s+.+$'
    first_h1 = re.search(title_pattern, content[frontmatter_end:], re.MULTILINE)
    if first_h1:
        insert_pos = frontmatter_end + first_h1.end()
    else:
        # No H1 found, insert at beginning
        insert_pos = 0

    # Find position of first ## heading
    first_h2_match = re.search(r'^##\s+', content[frontmatter_end:], re.MULTILINE)
    if first_h2_match:
        insert_pos = frontmatter_end + first_h2_match.start()
    elif first_h1:
        # Insert after H1
        insert_pos = frontmatter_end + first_h1.end()

    new_content = content[:insert_pos] + toc + content[insert_pos:]

    with open(filepath, 'w') as f:
        f.write(new_content)

    return True


def add_toc_instruction_to_skill(skill_content):
    """Add TOC requirement to a skill's creation instructions."""
    toc_instruction = '- **Include a Table of Contents** with internal anchor links for files with 2+ `##` sections'

    # Check if the specific instruction is already present
    if 'Include a Table of Contents' in skill_content:
        return False

    # Try to find a section for instructions/guidelines
    # Look for "## Instructions" or similar section headers
    instructions_match = re.search(r'^(##\s+Instructions\s+.*)', skill_content, re.MULTILINE)
    if instructions_match:
        insert_pos = instructions_match.end()
        new_content = (skill_content[:insert_pos] +
                       '\n' + toc_instruction +
                       skill_content[insert_pos:])
    else:
        # Find the first ## section and add before it
        first_section_match = re.search(r'^(##\s+.+)', skill_content, re.MULTILINE)
        if first_section_match:
            new_content = (skill_content[:first_section_match.start()] +
                           '\n' + toc_instruction +
                           '\n' + skill_content[first_section_match.start():])
        else:
            # Append at the end
            new_content = skill_content + '\n' + toc_instruction + '\n'

    return new_content


def main():
    base_dir = Path(__file__).parent.parent

    # Process .ai/ files
    ai_dir = base_dir / '.ai'
    laaw_dir = base_dir / 'LAAW'

    for target_dir in [ai_dir, laaw_dir]:
        if not target_dir.exists():
            continue

        for md_file in sorted(target_dir.rglob('*.md')):
            if add_toc_to_file(md_file):
                print(f'Added TOC: {md_file.relative_to(base_dir)}')

    # Update skills with TOC instruction
    for target_dir in [ai_dir, laaw_dir]:
        if not target_dir.exists():
            continue

        for skill_file in sorted(target_dir.rglob('SKILL.md')):
            with open(skill_file, 'r') as f:
                content = f.read()

            new_content = add_toc_instruction_to_skill(content)
            if new_content != content:
                with open(skill_file, 'w') as f:
                    f.write(new_content)
                print(f'Added TOC instruction: {skill_file.relative_to(base_dir)}')


if __name__ == '__main__':
    main()
