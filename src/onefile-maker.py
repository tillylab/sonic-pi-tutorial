import glob
import os

# Get list of markdown files from the specified directory
files = sorted(glob.glob("src/tutorial-de/*.md"))

toc = []
combined_content = []
toc_entries = []
current_top_level = None

for fname in files:
    with open(fname, "r") as infile:
        lines = infile.readlines()
        if not lines:
            continue

        # Extract the first line as the title
        title = lines[0].strip().lstrip("# ").strip()
        content = lines[3:]

        # Determine the section number
        base_name = os.path.basename(fname)
        section_number = base_name.split("-")[0]
        section_number_hyphened = section_number.replace(".", "-")

        if section_number.count('.') == 0:
            # Close the previous <ul> if there are any second-level entries
            if toc_entries:
                toc.append('<ul class="toc">')
                toc.extend(toc_entries)
                toc.append('</ul>')
                toc_entries = []

            # Top-level header
            toc.append(f'<li><a href="#section-{section_number_hyphened}">{section_number} {title}</a></li>')
            combined_content.append(f'# {title} {{#section-{section_number_hyphened}}}\n')
            current_top_level = section_number_hyphened
        else:
            # Second-level header
            toc_entries.append(f'  <li><a href="#section-{section_number_hyphened}">{section_number} {title}</a></li>')
            combined_content.append(f'## {title} {{#section-{section_number_hyphened}}}\n')

        combined_content.extend(content)
        combined_content.append("\n")

# Add the remaining second-level TOC entries inside a nested <ul> if there are any
if toc_entries:
    toc.append('<ul class="toc">')
    toc.extend(toc_entries)
    toc.append('</ul>')

# Write TOC to a file
with open("build/toc.html", "w") as tocfile:
    tocfile.write("\n".join(toc))
    print(f"Wrote table of contents to {tocfile.name}")

# Write combined content to a file
os.makedirs("build/tutorial-de-onefile", exist_ok=True)
with open("build/tutorial-de-onefile/index.md", "w") as outfile:
    outfile.write("".join(combined_content))
    print(f"Wrote monolithic markdown file to {outfile.name}")