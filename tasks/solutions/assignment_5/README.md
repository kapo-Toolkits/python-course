# tools — სასწავლო პაკეტი

პრაქტიკული დავალება #5-ის სანიმუშო ამოხსნა: წინა დავალებების ფუნქციები
ერთ პაკეტად აწყობილი.

## სტრუქტურა

```
assignment_5/
├── main.py            პროგრამის შესვლის წერტილი
├── .gitignore
├── README.md
└── tools/             პაკეტი
    ├── __init__.py    პაკეტის „ფასადი“
    ├── mathtools.py   is_prime · convert_temp · stats
    └── textutils.py   clean_word · count_vowels · unique_words · word_frequency
```

## გაშვება

```
python main.py                 # მთელი პროგრამა
python tools/mathtools.py      # მხოლოდ ამ მოდულის ტესტ-ბლოკი
python tools/textutils.py
```

## git — რას ველოდებით

```
git init
git add .gitignore README.md
git commit -m "პროექტის კარკასი: README და .gitignore"

git add tools/
git commit -m "tools პაკეტი: mathtools და textutils"

git add main.py
git commit -m "main.py — პაკეტის ფუნქციების დემონსტრაცია"
```

სამი commit, სამი დასრულებული ნაბიჯი. commit-ის შეტყობინება აღწერს,
**რა** გაკეთდა — არა „fix“, „update“, „asdf“.
