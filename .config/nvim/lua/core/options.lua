-- Line Numbers
vim.opt.number = true -- Show absolute line numbers
vim.opt.relativenumber = true -- Show relative line numbers

-- Clipboard
vim.o.clipboard = "unnamedplus" -- Use system clipboard

-- Line Wrapping
vim.opt.wrap = true -- Enable line wrapping
vim.opt.linebreak = true -- Break lines at word boundaries
vim.opt.breakindent = true -- Preserve indentation for wrapped lines
vim.opt.breakindentopt = "shift:4" -- Indent wrapped lines by 4 spaces more than the original line

-- Mouse Support
vim.o.mouse = "a" -- Enable mouse support in all modes

-- Indentation
vim.o.autoindent = true -- Copy indentation from previous line

vim.api.nvim_create_autocmd("FileType", {
	pattern = "lua,javascript,typescript,html,css,json,yaml",
	callback = function()
		vim.o.shiftwidth = 2
		vim.o.tabstop = 2
		vim.o.softtabstop = 2
		vim.o.expandtab = true -- Use spaces instead of tabs
	end,
})

vim.api.nvim_create_autocmd("FileType", {
	pattern = "python,rust",
	callback = function()
		vim.o.shiftwidth = 4
		vim.o.tabstop = 4
		vim.o.softtabstop = 4
		vim.o.expandtab = true
	end,
})

-- Go and Makefile should use hard tabs
vim.api.nvim_create_autocmd("FileType", {
	pattern = "go,make",
	callback = function()
		vim.o.shiftwidth = 4
		vim.o.tabstop = 4
		vim.o.softtabstop = 4
		vim.o.expandtab = false -- Use tabs instead of spaces
	end,
})

-- Search Settings
vim.o.ignorecase = true -- Case-insensitive search
vim.o.smartcase = true -- Case-sensitive if search includes uppercase

-- Scrolling
vim.opt.scrolloff = 8 -- Keep 8 lines visible above/below cursor
vim.opt.sidescrolloff = 8 -- Keep 8 columns visible left/right of cursor

-- Backspace Behavior
vim.o.backspace = "indent,eol,start" -- Allow backspacing over indentations, line breaks, and start of insert mode

-- Split Window Behavior
vim.o.splitright = true -- Open vertical splits to the right
vim.o.splitbelow = true -- Open horizontal splits below

-- Appearance
vim.o.termguicolors = true -- Enable 24-bit colors
vim.o.cursorline = true -- Highlight the cursor line
vim.o.showtabline = 2 -- Always show the tabline
vim.o.fileencoding = "utf-8" -- Set file encoding to UTF-8

-- Keyword Handling
vim.opt.iskeyword:append("-") -- Treat hyphenated words as a single word

-- Undo & Backup
vim.o.undofile = true -- Save undo history
vim.o.backup = false -- Disable backup file creation
vim.o.writebackup = false -- Prevent editing files opened by another program
vim.o.swapfile = false -- Disable swap file creation

-- Miscellaneous
vim.o.signcolumn = "yes" -- Keep sign column always visible
vim.o.completeopt = "menuone,noselect" -- Improve completion menu behavior
vim.o.numberwidth = 2 -- Set number column width to 2
vim.o.showmode = false -- Hide the mode display since the statusline already shows it
