-- Set leader key
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- For conciseness
local opts = { noremap = true, silent = true }

-- Disable the spacebar key's default behavior in Normal and Visual modes
vim.keymap.set({ "n", "v" }, "<Space>", "<Nop>", { silent = true })

-- General keymaps
vim.keymap.set("n", "<leader>wq", ":wq<CR>", opts)          -- save and quit
vim.keymap.set("n", "<leader>qq", ":q!<CR>", opts)          -- quit without saving
vim.keymap.set("n", "<leader>ww", ":w<CR>", opts)           -- save

vim.keymap.set("n", "<leader>wn", ":noautocmd w<CR>", opts) -- save file without auto-formatting
vim.keymap.set("n", "gx", ":!open <c-r><c-a><CR>", opts)    -- open URL under cursor

-- delete single character without copying into register
vim.keymap.set("n", "x", '"_x', opts)

-- Vertical scroll and center
vim.keymap.set("n", "<C-d>", "<C-d>zz", opts)
vim.keymap.set("n", "<C-u>", "<C-u>zz", opts)

-- Find and center
vim.keymap.set("n", "n", "nzzzv", opts)
vim.keymap.set("n", "N", "Nzzzv", opts)

-- Resize with arrows
vim.keymap.set("n", "<C-S-Up>", ":resize -2<CR>", opts)
vim.keymap.set("n", "<C-S-Down>", ":resize +2<CR>", opts)
vim.keymap.set("n", "<C-S-Left>", ":vertical resize -2<CR>", opts)
vim.keymap.set("n", "<C-S-Right>", ":vertical resize +2<CR>", opts)

-- Buffers
vim.keymap.set("n", "<Tab>", ":bnext<CR>", opts)
vim.keymap.set("n", "<S-Tab>", ":bprevious<CR>", opts)

-- Tab management
vim.keymap.set("n", "<leader>to", ":tabnew<CR>", opts)   -- open a new tab
vim.keymap.set("n", "<leader>tx", ":tabclose<CR>", opts) -- close a tab
vim.keymap.set("n", "<leader>tn", ":tabn<CR>", opts)     -- next tab
vim.keymap.set("n", "<leader>tp", ":tabp<CR>", opts)     -- previous tab

-- Split window management
vim.keymap.set("n", "<leader>sv", "<C-w>v", opts)     -- split window vertically
vim.keymap.set("n", "<leader>sh", "<C-w>s", opts)     -- split window horizontally
vim.keymap.set("n", "<leader>se", "<C-w>=", opts)     -- make split windows equal width
vim.keymap.set("n", "<leader>sx", ":close<CR>", opts) -- close split window

-- Navigate between splits
vim.keymap.set("n", "<C-h>", ":wincmd h<CR>", opts)
vim.keymap.set("n", "<C-j>", ":wincmd j<CR>", opts)
vim.keymap.set("n", "<C-k>", ":wincmd k<CR>", opts)
vim.keymap.set("n", "<C-l>", ":wincmd l<CR>", opts)

vim.keymap.set("n", "<C-Left>", ":wincmd h<CR>", opts)
vim.keymap.set("n", "<C-Up>", ":wincmd j<CR>", opts)
vim.keymap.set("n", "<C-Down>", ":wincmd k<CR>", opts)
vim.keymap.set("n", "<C-Right>", ":wincmd l<CR>", opts)

-- Toggle line wrapping
vim.keymap.set("n", "<leader>lw", "<cmd>set wrap!<CR>", opts)

-- Stay in indent mode
vim.keymap.set("v", "<", "<gv", opts)
vim.keymap.set("v", ">", ">gv", opts)

-- Keep last yanked when pasting
vim.keymap.set("v", "p", '"_dP', opts)

-- Diagnostic keymaps
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous diagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next diagnostic message" })
vim.keymap.set("n", "<leader>dd", vim.diagnostic.open_float, { desc = "Open floating diagnostic message" })

-- ThePrimeagen
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")
