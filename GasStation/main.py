def gasStation(gas, cost):
    cur_gas = 0
    total_gas = 0
    start_idx = 0
    for i in range(0, len(gas)):
        cur_gas += gas[i] - cost[i]
        total_gas += gas[i] - cost[i]
        if cur_gas < 0:
            # cannot start from that gas
            start_idx += 1;
            cur_gas = 0;
    return start_idx if total_gas >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
start = gasStation(gas, cost)
print(start)