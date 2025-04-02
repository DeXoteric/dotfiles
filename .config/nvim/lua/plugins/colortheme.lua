return {
	"catppuccin/nvim",
	name = "catppuccin",
	priority = 1000,
	opts = {
		flavour = "macchiato",
		no_italic = true,
		transparent_background = true,
		default_integrations = true,
	},
	config = function(_, opts)
		require("catppuccin").setup(opts)
		vim.cmd("colorscheme catppuccin")

		local bg_transparent = opts.transparent_background

		-- Toggle background transparency
		local toggle_transparency = function()
			bg_transparent = not bg_transparent
			opts.transparent_background = bg_transparent
			require("catppuccin").setup(opts)
			vim.cmd("colorscheme catppuccin")
			-- set_menu_border_transparency()
		end

		vim.keymap.set("n", "<leader>bg", toggle_transparency, { noremap = true, silent = true })
	end,
}
