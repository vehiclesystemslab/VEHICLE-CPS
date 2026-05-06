# PowerShell Deployment Steps — VEHICLE-CPS v1.1

## 1. Download and unzip the package

Download the ZIP package from ChatGPT and unzip it somewhere easy, for example:

```powershell
C:\Users\COREI7\Downloads\VEHICLE-CPS-v1.1-github-package
```

## 2. Open PowerShell

Go to the GitHub repository folder:

```powershell
cd "C:\Users\COREI7\Downloads\VEHICLE-CPS"
```

If the folder name is different, adjust the path.

## 3. Check the repo

```powershell
git status
```

You should see that you are inside a Git repository.

## 4. Copy the new package files into the repo

Option A: copy manually using Windows Explorer.

Option B: use PowerShell, adjusting the source path:

```powershell
Copy-Item -Path "C:\Users\COREI7\Downloads\VEHICLE-CPS-v1.1-github-package\*" -Destination "." -Recurse -Force
```

## 5. Check changes

```powershell
git status
```

You should see modified and new files such as:

- README.md
- ETHICS.md
- ROADMAP.md
- CITATION.cff
- requirements.txt
- docs/
- assets/
- examples/
- src/

## 6. Test the Python demo

Optional but recommended:

```powershell
python examples\run_synthetic_demo.py
```

If Python packages are missing:

```powershell
pip install -r requirements.txt
python examples\run_synthetic_demo.py
```

## 7. Commit and push

```powershell
git add .
git commit -m "Rebuild VEHICLE-CPS v1.1 repository"
git push
```

## 8. Verify on GitHub

Open:

```text
https://github.com/vehiclesystemslab/VEHICLE-CPS
```

Check that the new README appears correctly.
