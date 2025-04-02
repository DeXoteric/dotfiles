return {
	"nvim-telescope/telescope.nvim",
	branch = "0.1.x",
	dependencies = {
		"nvim-lua/plenary.nvim",
		{
			"nvim-telescope/telescope-fzf-native.nvim",
			build = "make",
			cond = function()
				return vim.fn.executable("make") == 1
			end,
		},
		"nvim-telescope/telescope-ui-select.nvim",
		"nvim-tree/nvim-web-devicons",
	},
	config = function()
		local actions = require("telescope.actions")
		local builtin = require("telescope.builtin")

		require("telescope").setup({
			defaults = {
				mappings = {
					i = {
						["<C-k>"] = actions.move_selection_previous, -- move to prev result
						["<C-j>"] = actions.move_selection_next, -- move to next result
					},
				},
			},
			pickers = {
				find_files = {
					file_ignore_patterns = { "node_modules", ".git", ".venv" },
					hidden = true,
				},
			},
			live_grep = {
				file_ignore_patterns = { "node_modules", ".git", ".venv" },
				additional_args = function(_)
					return { "--hidden" }
				end,
			},
			path_display = {
				filename_first = {
					reverse_directories = true,
				},
			},
			extensions = {
				["ui-select"] = {
					require("telescope.themes").get_dropdown(),
				},
			},
			git_files = {
				previewer = false,
			},
		})

		-- Enable telescope fzf native, if installed
		pcall(require("telescope").load_extension, "fzf")
		pcall(require("telescope").load_extension, "ui-select")

		-- Keymaps
		vim.keymap.set("n", "<leader>f?", builtin.oldfiles, { desc = "Find recently opened files" })
		vim.keymap.set("n", "<leader>fb", builtin.buffers, { desc = "Search existing buffers" })
		vim.keymap.set("n", "<leader>ff", builtin.find_files, { desc = "Search files" })
		vim.keymap.set("n", "<leader>fh", builtin.help_tags, { desc = "Search help" })
		vim.keymap.set("n", "<leader>fw", builtin.grep_string, { desc = "Search selected word" })
		vim.keymap.set("n", "<leader>fg", builtin.live_grep, { desc = "Search by grep" })
		vim.keymap.set("n", "<leader>fd", builtin.diagnostics, { desc = "Search diagnostics" })
		vim.keymap.set("n", "<leader>fds", function()
			builtin.lsp_document_symbols({
				symbols = { "Class", "Function", "Method", "Constructor", "Interface", "Module", "Property" },
			})
		end, { desc = "Seach LSP document symbols" })
		vim.keymap.set("n", "<leader>f/", function()
			-- You can pass additional configuration to telescope to change theme, layout, etc.
			builtin.current_buffer_fuzzy_find(require("telescope.themes").get_dropdown({
				previewer = false,
			}))
		end, { desc = "Fuzzily search in current buffer" })
	end,
}
