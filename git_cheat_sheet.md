
# Git Cheat Sheet – Shadowrun Character Creator Edition

## 🛠 Daily Workflow

```bash
git add .
git commit -m "Describe what you changed"
git push
```

## 🧳 Cloning Your Repo on Another Machine

```bash
git clone git@github.com:Ondrarepka/shadowrun-char-creator.git
```

## 🔗 Checking & Switching to SSH Remote

```bash
git remote -v
git remote set-url origin git@github.com:USERNAME/REPO.git
```

## 🌿 Working with Branches

```bash
# Create and switch to a new branch
git checkout -b feature-name

# Make changes, then:
git add .
git commit -m "Work on feature"
git push -u origin feature-name
```

## 🔄 Syncing With GitHub

```bash
git pull
git pull --rebase  # preferred for clean history
```

## 🚑 Common Fixes

- **Remote contains work you don’t have:**

```bash
git pull --rebase origin main
```

- **Undo last commit (keep changes):**

```bash
git reset --soft HEAD~1
```

- **Unstage a file:**

```bash
git reset HEAD <file>
```

## ✅ Good Practices

- Commit often and clearly
- Use branches for experiments or features
- Push before switching computers or ending your session
