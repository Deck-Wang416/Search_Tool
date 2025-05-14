from crawler import crawl_website
from indexer import (
    build_index, save_index, load_index, print_word, find_phrase
)

def main():
    index = None
    loaded = False

    while True:
        try:
            command = input("\nEnter command (build, load, print <word>, find <phrase>, exit): ").strip()
            if command == "exit":
                print("Goodbye!")
                break

            elif command == "build":
                pages = crawl_website()
                index = build_index(pages)
                save_index(index)
                print("Index built and saved.")
                loaded = True

            elif command == "load":
                index = load_index()
                print("Index loaded from file.")
                loaded = True

            elif command.startswith("print "):
                if not loaded:
                    print("Please build or load the index first.")
                    continue
                word = command[6:].strip()
                print_word(index, word)

            elif command.startswith("find "):
                if not loaded:
                    print("Please build or load the index first.")
                    continue
                phrase = command[5:].strip()
                result = find_phrase(index, phrase)
                if result:
                    print("Pages containing the phrase:")
                    for url in result:
                        print(f"  {url}")
                else:
                    print("No pages found containing all the search terms.")

            else:
                print("Invalid command.")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting...")
            break

if __name__ == "__main__":
    main()
