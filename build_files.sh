# build_files.sh

echo "BUILD START"
pip install -r requirements.txt
python3.x manage.py collectstatic --no-input --clear
echo "BUILD END"