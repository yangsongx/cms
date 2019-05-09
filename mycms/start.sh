#!/bin/bash
NAME="mtest"         # Name of the application
DJANGODIR=/opt/mytest # Django project directory
SOCKFILE=/opt/mytest/run/gunicorn.sock  # we will communicte using this unix socket
USER=root                                        # the user to run as
GROUP=root                                     # the group to run as
NUM_WORKERS=4                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=mycms.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=mycms.wsgi                     # WSGI module name

rm $SOCKFILE

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
#source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn -k gevent ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --worker-connections 2048 \
  --bind=unix:$SOCKFILE \
  --backlog 4096 \
  --log-level=debug \
  --log-file=-

