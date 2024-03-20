Создать ssh ключ:
1) ssh-keygen -t ed25519 -C "почта"
2) cat <название файла.pub>
3) eval "$(ssh-agent -s)"
4) ssh-add <название файла>
5) создать ключ на сайте
6) ssh -T git@github.com
Клонировать репозиторий:
git clone <url>
Проверить статус:
git status