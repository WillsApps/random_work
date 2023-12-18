base_xp = 1.0
verdant_xp_mod = 0.45

base_monster_generation_rate = 1.0
base_duration = 300
teal_duration_mod = -50
teal_number_monster_mod = 0.3
base_number_monster = base_monster_generation_rate / base_duration


for teal_count in range(4):
    verdant_count = 3 - teal_count
    xp_mod = base_xp + verdant_xp_mod * verdant_count

    duration_mod = base_duration + teal_duration_mod * teal_count
    percent_duration_change = duration_mod / base_duration

    monster_generation_rate_mod = (
        base_monster_generation_rate + teal_number_monster_mod * teal_count
    )
    total_monsters = monster_generation_rate_mod * duration_mod
    monster_ratio = total_monsters / base_duration
    xp_ratio = xp_mod * monster_ratio
    xp_per_second = (xp_ratio / duration_mod) * 10000
    print(
        ", ".join(
            [
                f"{teal_count=}",
                f"{verdant_count=}",
                f"{xp_mod=}",
                f"{monster_generation_rate_mod=}",
                f"{duration_mod=}",
                f"{percent_duration_change=}",
                f"{total_monsters=}",
                f"{xp_ratio=}",
                f"{xp_per_second=}",
            ]
        )
    )
