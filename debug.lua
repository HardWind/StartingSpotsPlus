function debugPrint(msg)
	for _, player in pairs(game.players) do
		player.print(tostring(msg))
	end
end