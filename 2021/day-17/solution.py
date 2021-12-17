# DAY 17
from itertools import product

# Today, I'm lazy on the input parsing.:)
target_x = (169, 206)
target_y = (-108, -68)


def fire_probe(vx, vy):
    x, y = 0, 0
    while True:
        # The probe's x position increases by its x velocity.
        # The probe's y position increases by its y velocity.
        x, y = x + vx, y + vy

        # Due to drag, the probe's x velocity changes by 1 toward the value 0;
        # that is, it decreases by 1 if it is greater than 0, increases by 1 if
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1

        # Due to gravity, the probe's y velocity decreases by 1.
        vy -= 1

        yield x, y


def reached_target(x, y):
    return (
        x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]
    )


def missed_target(x, y):
    return x > target_x[1] or y < target_y[0]


def brute_force_velocity():
    good_velocities = []
    for vx, vy in product(range(500), range(-500, 500)):
        largest_y = 0
        for x, y in fire_probe(vx, vy):
            largest_y = y if y > largest_y else largest_y
            if reached_target(x, y):
                good_velocities.append((vx, vy, largest_y))
                break
            elif missed_target(x, y):
                break
    return max(largest_y for _, _, largest_y in good_velocities), len(good_velocities)


print("Part 1")
largest_y, total_possible_velocities = brute_force_velocity()
print(largest_y)

print("Part 2")
print(total_possible_velocities)
