TODAY=$(date +"%Y-%m-%d")
END_TIME="${TODAY}T23:59:59"

CLUSTER_IDENTIFIER=$1
SCHEDULED_ACTION_NAME=pause-"$CLUSTER_IDENTIFIER"-"$TODAY"
# Role needs schedule permissions
IAM_ROLE=$2

echo "Resuming: ${CLUSTER_IDENTIFIER}"
echo "ScheduleName: ${SCHEDULED_ACTION_NAME}"
echo "ScheduleTime (UTC): ${END_TIME}"
echo ""
echo "Resume Status:"
aws redshift resume-cluster \
  --cluster-identifier=$CLUSTER_IDENTIFIER \
  --no-cli-pager | \
  grep "ClusterStatus"

echo ""
echo "Schedule Status:"
aws redshift create-scheduled-action \
  --scheduled-action-name="$SCHEDULED_ACTION_NAME" \
  --target-action=PauseCluster="{ClusterIdentifier=$CLUSTER_IDENTIFIER}" \
  --schedule="at($END_TIME)" \
  --iam-role="$IAM_ROLE" \
  --no-cli-pager | \
  grep "ScheduledActionName\|Schedule"

/Users/wburdett/.PyCharm/scratches/extensions/mine/_aliases/redshift-watch.sh
