extends CharacterBody2D

@export var speed = 400

func get_input():
	look_at(get_global_mouse_position())
	# velocity = transform.x * Input.get_axis("down", "up") * speed
	# velocity += transform.y * Input.get_axis("left", "right") * speed
	velocity = Vector2(
		Input.get_axis("left", "right") * speed,
		Input.get_axis("down", "up") * -1 * speed
	)


func _physics_process(delta):
	get_input()
	move_and_slide()
