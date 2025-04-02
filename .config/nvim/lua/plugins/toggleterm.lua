return {
	-- https://github.com/akinsho/toggleterm.nvim
	"akinsho/toggleterm.nvim",
	version = "*",
	opts = {
		open_mapping = [[<C-\>]],
		shade_terminals = false,
		start_in_insert = true,
		-- direction = "float",
		insert_mappings = true,
		persist_size = true,
		close_on_exit = true,
	},
}
