from dataclasses import dataclass

RAGE_LOST_BASE = 5
RAGE_LOST_ACCELERATION = 0.1
HELM_ENCHANT_MODIFIER = 1
COOLDOWN = 5
MAX_RAGE = 50
CURRENT_RAGE = MAX_RAGE
CURRENT_RAGE = min(CURRENT_RAGE, MAX_RAGE)


@dataclass
class Result:
    rage_generation: int
    berserker_length: int
    max_rage_length: int
    total_length: int
    uptime: float


RESULTS = []
for helm_enchant_modifier in (0.6, 1):
    for rage_generation in range(1, 25):
        berserker_length = 0
        CURRENT_RAGE = 100
        CURRENT_RAGE = min(CURRENT_RAGE, MAX_RAGE)
        RAGE_LOST_BASE = 5
        for i in range(1, 100):
            if CURRENT_RAGE < 0:
                berserker_length = i
                break
            RAGE_LOST_BASE += helm_enchant_modifier * (RAGE_LOST_BASE * RAGE_LOST_ACCELERATION)
            CURRENT_RAGE -= RAGE_LOST_BASE
            CURRENT_RAGE += rage_generation
            CURRENT_RAGE = min(CURRENT_RAGE, MAX_RAGE)
        max_rage_length = 0
        CURRENT_RAGE = 0
        for i in range(1, 100):
            # print(f"{i=}, {current_rage=}")
            if CURRENT_RAGE > MAX_RAGE:
                max_rage_length = i
                break
            CURRENT_RAGE += rage_generation
        total_length = berserker_length + max_rage_length
        uptime = berserker_length / total_length
        RESULTS.append(
            Result(
                rage_generation=rage_generation,
                berserker_length=berserker_length,
                max_rage_length=max_rage_length,
                total_length=total_length,
                uptime=uptime,
            )
        )
        # print(f"{rage_generation=}, {berserker_length=}, {max_rage_length=}, {total_length=}, {uptime=}")

for result in RESULTS:
    print(result)
