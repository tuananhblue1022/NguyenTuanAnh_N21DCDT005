class DictionaryEntry:
    def __init__(self, word):
        self.word = word
        self.meanings = []

    def add_meaning(self, part_of_speech, meaning, example):
        self.meanings.append({
            'part_of_speech': part_of_speech,
            'meaning': meaning,
            'example': example
        })

class Dictionary:
    def __init__(self):
        self.entries = []

    def add_entry(self, word, part_of_speech, meaning, example):
        for entry in self.entries:
            if entry.word == word:
                entry.add_meaning(part_of_speech, meaning, example)
                self.entries.sort(key=lambda x: x.word)
                return
        new_entry = DictionaryEntry(word)
        new_entry.add_meaning(part_of_speech, meaning, example)
        self.entries.append(new_entry)
        self.entries.sort(key=lambda x: x.word)

    def remove_entry(self, word):
        self.entries = [entry for entry in self.entries if entry.word != word]

    def lookup(self, word):
        for entry in self.entries:
            if entry.word == word:
                return entry
        return None

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for entry in self.entries:
                f.write(entry.word + '\n')
                for meaning in entry.meanings:
                    line = f"  {meaning['part_of_speech']} | {meaning['meaning']} | {meaning['example']}\n"
                    f.write(line)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.entries = []
                lines = f.readlines()
                current_word = None
                for line in lines:
                    if not line.startswith("  "):
                        current_word = line.strip()
                        entry = DictionaryEntry(current_word)
                        self.entries.append(entry)
                    else:
                        part_of_speech, meaning, example = map(str.strip, line.strip().split('|'))
                        self.entries[-1].add_meaning(part_of_speech, meaning, example)
        except FileNotFoundError:
            print(f"File {filename} không tồn tại. Bắt đầu với từ điển trống.")
            self.entries = []

def menu():
    dictionary = Dictionary()
    filename = "NguyenTuanAnh_N21DCDT005.txt"

    while True:
        print("\nMenu")
        print("1. Thêm một mục từ mới")
        print("2. Loại bỏ một mục từ")
        print("3. Tra cứu các nghĩa của một mục từ")
        print("4. Lưu từ điển vào tập tin")
        print("5. Nạp từ điển từ tập tin")
        print("6. Thoát chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            word = input("Nhập từ: ")
            part_of_speech = input("Nhập loại từ (danh từ, động từ, tính từ): ")
            meaning = input("Nhập nghĩa của từ: ")
            example = input("Nhập ví dụ: ")
            dictionary.add_entry(word, part_of_speech, meaning, example)
        elif choice == '2':
            word = input("Nhập từ cần loại bỏ: ")
            dictionary.remove_entry(word)
        elif choice == '3':
            word = input("Nhập từ cần tra cứu: ")
            entry = dictionary.lookup(word)
            if entry:
                print(f"\nTừ: {entry.word}")
                for meaning in entry.meanings:
                    print(f"Loại từ: {meaning['part_of_speech']}")
                    print(f"Nghĩa: {meaning['meaning']}")
                    print(f"Ví dụ: {meaning['example']}\n")
            else:
                print("Không tìm thấy từ.")
        elif choice == '4':
            dictionary.save_to_file(filename)
            print(f"Từ điển đã được lưu vào {filename}")
        elif choice == '5':
            dictionary.load_from_file(filename)
            print(f"Từ điển đã được nạp từ {filename}")
        elif choice == '6':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    menu()
