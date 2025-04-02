return {
  "nvim-lualine/lualine.nvim",
  dependencies = {
    -- https://github.com/nvim-tree/nvim-web-devicons
    "nvim-tree/nvim-web-devicons",  -- fancy icons
    -- https://github.com/linrongbin16/lsp-progress.nvim
    "linrongbin16/lsp-progress.nvim", -- LSP loading progress
  },
  opts = {
    options = {
      theme = "catppuccin", -- "auto, tokyonight, catppuccin, codedark, nord"
      component_separators = { left = "", right = "" },
      section_separators = { left = "", right = "" },
    },
    sections = {
      lualine_c = {
        {
          "filename",
          file_status = true, -- Displays file status (readonly status, modified status)
          newfile_status = false, -- Display new file status (new file means no write after created)
          path = 0,          -- 0: Just the filename
          -- 1: Relative path
          -- 2: Absolute path
          -- 3: Absolute path, with tilde as the home directory
          -- 4: Filename and parent dir, with tilde as the home directory
          symbols = {
            modified = "[+]", -- Text to show when the file is modified.
            readonly = "[-]", -- Text to show when the file is non-modifiable or readonly.
          },
        },
      },
      lualine_x = {
        "encoding",
        "filetype",
      },
    },
    extensions = { "fugitive" },
  },
}
