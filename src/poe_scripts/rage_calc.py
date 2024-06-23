from dataclasses import dataclass

COOLDOWN = 5
MAX_RAGE = 130


@dataclass
class Skill:
    name: str
    rage_lost_base: int
    rage_lost_acceleration: float
    cooldown: int = None


SKILLS = [
    Skill(
        name="Berserk",
        rage_lost_base=5,
        rage_lost_acceleration=0.1,
        cooldown=5,
    ),
    Skill(name="Rage Vortex", rage_lost_base=3, rage_lost_acceleration=0.2),
]


@dataclass
class Result:
    rage_generation: int
    length: int
    max_rage_length: int
    total_length: int
    uptime: float


def get_results_for_skill(skill: Skill):
    results = []
    for rage_generation in range(1, 30):
        berserker_length = 0
        current_rage = 120
        current_rage = min(current_rage, MAX_RAGE)
        rage_lost_base = skill.rage_lost_base
        for i in range(1, 100):
            if current_rage < 0:
                berserker_length = i
                break
            rage_lost_base += rage_lost_base * skill.rage_lost_acceleration
            current_rage -= rage_lost_base
            current_rage += rage_generation
            current_rage = min(current_rage, MAX_RAGE)
        max_rage_length = 0
        current_rage = 0
        for i in range(1, 100):
            # print(f"{i=}, {current_rage=}")
            if current_rage > MAX_RAGE:
                max_rage_length = i
                break
            current_rage += rage_generation
        total_length = berserker_length + max_rage_length
        uptime = berserker_length / total_length
        results.append(
            Result(
                rage_generation=rage_generation,
                length=berserker_length,
                max_rage_length=max_rage_length,
                total_length=total_length,
                uptime=uptime,
            )
        )
        # print(f"{rage_generation=}, {berserker_length=}, {max_rage_length=}, {total_length=}, {uptime=}")
    return results

def main():
    for skill in SKILLS:
        results = get_results_for_skill(skill)
        print(f"{skill.name=}")
        for result in results:
            print(result)

if __name__ == '__main__':
    main()
