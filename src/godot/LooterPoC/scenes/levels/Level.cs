using Godot;
using System;

public partial class Level : Node2D
{
	// private Sprite2D _logo;
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		// _logo = GetNode<Sprite2D>("Logo");
		// _logo.Rotation = 90;

	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
		if (Input.IsActionPressed("quit"))
		{
			GetTree().Root.PropagateNotification((int)NotificationWMCloseRequest);
			GetTree().Quit();
		}
		if (Input.IsActionPressed("left")) {

		}
		// _logo.Rotation += 10 * (float)delta;
		// if (_logo.Rotation > 180)
		// {
			// _logo.Rotation = 0;
		// }
		// if (_logo.Position.X > 1000)
		// {
		// 	_logo.Position = new Vector2(0, _logo.Position.Y);
		// }
	}
}
