using Godot;
using System;

public partial class Player : CharacterBody2D
{
	private const int Speed = 500;
	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Vector2 direction = Input.GetVector("left", "right", "up", "down");
		Velocity = direction * Speed;
		MoveAndSlide();
		// Position += direction * Speed * (float)delta;

		if (Input.IsActionPressed("primary_action"))
		{
			GD.Print("Shoot Laser");
		}

		if (Input.IsActionPressed("secondary_action"))
		{
			GD.Print("Shoot Grenade");
		}
	}
}
