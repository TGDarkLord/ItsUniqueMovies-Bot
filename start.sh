if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TGDarkLord/MovieClub-Robot.git /MovieClub-Robot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MovieClub-Robot
fi
cd /MovieClub-Robot
pip3 install -U -r requirements.txt
echo "Starting MovieClub RoBot...🤖"
python3 bot.py
