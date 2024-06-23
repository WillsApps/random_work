using Godot;
using System;

public partial class drone : CharacterBody2D
{
	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		Vector2 direction = Vector2.Right;
		Velocity = direction * 150;
		MoveAndSlide();
	}
}
