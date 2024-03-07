#!/usr/bin/env python3

def file_extensions(filename):
    file_no_extension = []
    file_w_extension = {}
    with open(filename) as file:
        for line in file:
            line_strip = line.rstrip("\n")
            try:
                
                line_split = line_strip.rsplit(".", 1)  # only split one time, and it should be the last "."
                f_name, f_type = line_split[0], line_split[1]
                if not f_type in file_w_extension:
                    file_w_extension[f_type] = [line_strip]
                
                else:
                    file_w_extension[f_type].append(line_strip)
            
            except: # catch the files without type and no "."
                file_no_extension.append(line_strip)

    
    return (file_no_extension, file_w_extension)

def main():
    file_no_extension, file_w_extension = file_extensions("src/filenames.txt")

    print(f"{len(file_no_extension)} files with no extension")
    for key, value in file_w_extension.items():
        print(f"{key} {len(value)}")

if __name__ == "__main__":
    main()
