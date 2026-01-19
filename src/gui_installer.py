#!/usr/bin/env python3
"""
xsvStudio GUI Installer - v5.0 (Safety Protocols & Service Coding)

Author: xsvStudio Technology Division
Date: 2026-01-18
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import threading
from pathlib import Path
import datetime
import webbrowser
import json

# FIX: Robust Import Strategy
CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

try:
    from init_company_structure import CompanyStructureBuilder
except ImportError:
    try:
        sys.path.append(str(CURRENT_DIR.parent / "scripts"))
        from init_company_structure import CompanyStructureBuilder
    except ImportError:
        CompanyStructureBuilder = None

# --- DESIGN SYSTEM: "VOID NEON" ---
COLOR_BG = "#050505"
COLOR_SURFACE = "#111111"
COLOR_BORDER = "#333333"

# Brand Colors
COLOR_BRAND_MAIN = "#6C5CE7" 
COLOR_BRAND_DOT = "#FF7675"  
COLOR_TEXT_MAIN = "#FFFFFF"
COLOR_TEXT_DIM = "#666666"
COLOR_LOCKED = "#2A2A2A"

# Status Colors
COLOR_SUCCESS = "#00B894"
COLOR_ERROR = "#FF7675"
COLOR_WARNING = "#FDCB6E"

# Fonts
FONT_HERO = ("Segoe UI", 36, "bold")
FONT_NAV = ("Segoe UI", 11, "bold")
FONT_H2 = ("Segoe UI", 12, "bold")
FONT_BODY = ("Segoe UI", 10)
FONT_MONO = ("Consolas", 9)

class ModernScrollbar(tk.Canvas):
    """ Custom Canvas-based Scrollbar """
    def __init__(self, master, target_widget=None, bg=COLOR_BG, thumb_color=COLOR_BRAND_MAIN, **kwargs):
        super().__init__(master, width=12, bg=bg, highlightthickness=0, **kwargs)
        self.target = target_widget
        self.thumb_color = thumb_color
        self.y_top = 0
        self.y_bottom = 0
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        
    def set(self, first, last):
        self.y_top = float(first)
        self.y_bottom = float(last)
        self.redraw()

    def redraw(self):
        self.delete("all")
        h = self.winfo_height()
        if h == 0: return
        self.create_rectangle(0, 0, 12, h, fill="#0F0F0F", outline="")
        start_y = self.y_top * h
        end_y = self.y_bottom * h
        min_len = 20
        if end_y - start_y < min_len: end_y = start_y + min_len
        self.create_rectangle(2, start_y, 10, end_y, fill=self.thumb_color, outline="", tags="thumb")

    def on_click(self, event):
        self.on_drag(event)

    def on_drag(self, event):
        h = self.winfo_height()
        if h == 0: return
        frac = event.y / h
        self.target.yview_moveto(frac)

class ModernToggle(tk.Canvas):
    def __init__(self, master, variable, command=None, state='normal', *args, **kwargs):
        super().__init__(master, width=44, height=24, bg=COLOR_SURFACE, highlightthickness=0, *args, **kwargs)
        self.variable = variable
        self.command = command
        self.state_val = state
        if self.state_val == 'normal': self.bind("<Button-1>", self.toggle)
        self.variable.trace_add("write", self.update_visual)
        self.update_visual()

    def toggle(self, event=None):
        if self.state_val == 'disabled': return
        self.variable.set(not self.variable.get())
        if self.command: self.command()

    def update_visual(self, *args):
        self.delete("all")
        is_on = self.variable.get()
        if self.state_val == 'disabled':
            fill = "#333333"
            thumb_fill = "#555555"
        else:
            fill = COLOR_BRAND_MAIN if is_on else "#333333"
            thumb_fill = "#FFFFFF"
        self.create_rounded_rect(2, 2, 42, 22, 10, fill, outline="")
        x = 32 if is_on else 12
        self.create_oval(x-8, 4, x+8, 20, fill=thumb_fill, outline="")

    def create_rounded_rect(self, x1, y1, x2, y2, r, fill, outline):
        points = [x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1]
        return self.create_polygon(points, fill=fill, smooth=True)

class ModernButton(tk.Label):
    def __init__(self, master, text, command, bg=COLOR_BRAND_MAIN, fg="#FFFFFF", font=None, **kwargs):
        if font is None: font=("Segoe UI", 11, "bold")
        super().__init__(master, text=text, bg=bg, fg=fg, font=font, cursor="hand2", pady=10, **kwargs)
        self.bind("<Button-1>", lambda e: command())

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Operations Evolved - xsvStudio")
        self.geometry("1100x900")
        self.configure(bg=COLOR_BG)
        self.state('zoomed')
        
        # State
        self.is_premium = False
        self.installed_path = None
        
        # Data
        self.company_name = tk.StringVar()
        self.install_path = tk.StringVar(value=str(Path.home() / 'Documents'))
        self.current_tab = "INSTALLER"
        
        # Naming Rule Data
        self.naming_rule = tk.StringVar(value="service_code")
        self.custom_format = tk.StringVar(value="[YYYY][MM][DD]-[SERVICE]-[CLIENT]")
        
        # Features & Services
        self.features = {
            'structure': tk.BooleanVar(value=True),
            'autofile': tk.BooleanVar(value=False),
            'audit': tk.BooleanVar(value=False),
            'git_init': tk.BooleanVar(value=False),
            'naming_engine': tk.BooleanVar(value=True)
        }
        self.services = {
            'WEB': tk.BooleanVar(value=True),
            'IT': tk.BooleanVar(value=True),
            'CM': tk.BooleanVar(value=True),
            'MFG': tk.BooleanVar(value=True),
            'TECH': tk.BooleanVar(value=True),
            'LEGAL': tk.BooleanVar(value=True),
            'MS': tk.BooleanVar(value=True),
            'MULTI': tk.BooleanVar(value=True)
        }
        
        self.check_license_file()
        self.setup_ui()
        
    def check_license_file(self):
        lic_path = Path("xsv_license.key")
        if lic_path.exists():
            self.is_premium = True
            
    def setup_ui(self):
        # --- HEADER ---
        header = tk.Frame(self, bg=COLOR_BG, height=80)
        header.pack(fill='x', padx=50, pady=20)
        
        logo_frame = tk.Frame(header, bg=COLOR_BG)
        logo_frame.pack(side='left')
        tk.Label(logo_frame, text="xsv", font=FONT_HERO, fg=COLOR_BRAND_MAIN, bg=COLOR_BG).pack(side='left', padx=0)
        tk.Label(logo_frame, text="Studio", font=FONT_HERO, fg="#FFFFFF", bg=COLOR_BG).pack(side='left', padx=0)
        tk.Label(logo_frame, text=".", font=FONT_HERO, fg=COLOR_BRAND_DOT, bg=COLOR_BG).pack(side='left', padx=0)

        nav_frame = tk.Frame(header, bg=COLOR_BG)
        nav_frame.pack(side='right', pady=15)
        
        self.btn_nav_install = self.create_nav_btn(nav_frame, "INSTALLER", "INSTALLER")
        
        # --- MAIN CONTAINER ---
        self.container = tk.Frame(self, bg=COLOR_BG)
        self.container.pack(fill='both', expand=True, padx=50)

        self.view_installer = tk.Frame(self.container, bg=COLOR_BG)
        
        self.setup_installer_view()
        
        self.switch_tab("INSTALLER")

    def create_nav_btn(self, parent, text, tab_id):
        l = tk.Label(parent, text=text, font=FONT_NAV, fg=COLOR_TEXT_DIM, bg=COLOR_BG, cursor="hand2")
        l.pack(side='left', padx=15)
        l.bind("<Button-1>", lambda e: self.switch_tab(tab_id))
        return l

    def switch_tab(self, tab_name):
        self.current_tab = tab_name
        self.view_installer.pack_forget()
        
        self.btn_nav_install.config(fg=COLOR_TEXT_DIM)
        
        if tab_name == "INSTALLER":
            self.view_installer.pack(fill='both', expand=True)
            self.btn_nav_install.config(fg="white")

    def setup_installer_view(self):
        grid = self.view_installer
        left = tk.Frame(grid, bg=COLOR_BG)
        left.pack(side='left', fill='both', expand=True, padx=(0, 25))
        right = tk.Frame(grid, bg=COLOR_BG, width=420)
        right.pack(side='right', fill='y', padx=(25, 0))
        right.pack_propagate(False)

        # -- Identity --
        self.card_header(left, "01 / IDENTITY")
        ident_card = tk.Frame(left, bg=COLOR_SURFACE, padx=20, pady=20)
        ident_card.pack(fill='x', pady=(0, 20))
        tk.Label(ident_card, text="Organization Name", bg=COLOR_SURFACE, fg=COLOR_TEXT_DIM, font=FONT_BODY).pack(anchor='w')
        tk.Entry(ident_card, textvariable=self.company_name, bg=COLOR_BG, fg="white", font=("Segoe UI", 12), relief="flat", insertbackground="white").pack(fill='x', pady=(5, 10), ipady=8)
        tk.Label(ident_card, text="Root Directory", bg=COLOR_SURFACE, fg=COLOR_TEXT_DIM, font=FONT_BODY).pack(anchor='w')
        dir_frm = tk.Frame(ident_card, bg=COLOR_BG)
        dir_frm.pack(fill='x', pady=5)
        tk.Entry(dir_frm, textvariable=self.install_path, bg=COLOR_BG, fg="#888", font=("Segoe UI", 10), relief="flat", state='readonly').pack(side='left', fill='x', expand=True, ipady=8, padx=10)
        tk.Button(dir_frm, text="BROWSE", command=self.browse, bg=COLOR_SURFACE, fg="white", relief="flat", cursor="hand2").pack(side='right', padx=2)

        # -- Services --
        self.card_header(left, "02 / SERVICE MODULES")
        srv_card = tk.Frame(left, bg=COLOR_SURFACE, padx=20, pady=20)
        srv_card.pack(fill='x', pady=(0, 20))
        if not self.is_premium:
            tk.Label(srv_card, text="FREE VERSION - ALL SERVICES ENABLED", fg=COLOR_SUCCESS, bg=COLOR_SURFACE, font=("Segoe UI", 9, "bold")).grid(row=0, column=0, columnspan=3, sticky='w', pady=(0,10))
        r=1; c=0
        for code, var in self.services.items():
            f = tk.Frame(srv_card, bg=COLOR_SURFACE)
            f.grid(row=r, column=c, sticky='w', padx=10, pady=5)
            state = 'normal'
            ModernToggle(f, var, state=state).pack(side='left')
            lbl_color = "white" if state == 'normal' else "#444"
            tk.Label(f, text=code, bg=COLOR_SURFACE, fg=lbl_color, font=FONT_BODY, padx=10).pack(side='left')
            c += 1
            if c > 2: c=0; r+=1
        srv_card.grid_columnconfigure(0, weight=1)
        srv_card.grid_columnconfigure(1, weight=1)
        srv_card.grid_columnconfigure(2, weight=1)

        # -- Console --
        tk.Label(right, text="SYSTEM LOG", font=("Consolas", 10, "bold"), fg=COLOR_BRAND_MAIN, bg=COLOR_BG).pack(anchor='w', pady=(0, 10))
        console_frm = tk.Frame(right, bg=COLOR_SURFACE)
        console_frm.pack(fill='both', expand=True)
        self.console = tk.Text(console_frm, bg=COLOR_SURFACE, fg="#CCCCCC", font=("Consolas", 9), relief="flat", padx=15, pady=15, insertbackground="white", wrap="word")
        self.console.pack(side='left', fill='both', expand=True)
        sb = ModernScrollbar(console_frm, target_widget=self.console, bg=COLOR_SURFACE)
        sb.pack(side='right', fill='y')
        self.console.config(yscrollcommand=sb.set)
        
        self.console.tag_config("green", foreground=COLOR_SUCCESS)
        self.console.tag_config("red", foreground=COLOR_ERROR)
        self.console.tag_config("warn", foreground=COLOR_WARNING)
        
        init_msg = "> Operations Evolved v1.0\n> System initialized...\n"
        self.console.insert("end", init_msg)
        self.console.config(state='disabled')

        self.progress_canvas = tk.Canvas(right, height=4, bg=COLOR_SURFACE, highlightthickness=0)
        self.progress_canvas.pack(fill='x', pady=(20, 0))
        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, 4, fill=COLOR_SUCCESS, width=0)

        self.btn_run = ModernButton(right, text="INITIALIZE SYSTEMS", command=self.confirm_and_run)
        self.btn_run.pack(fill='x', pady=20)

    def card_header(self, parent, text):
        tk.Label(parent, text=text, font=("Segoe UI", 9, "bold"), fg=COLOR_BRAND_MAIN, bg=COLOR_BG).pack(anchor='w', pady=(0, 8))

    def browse(self):
        d = filedialog.askdirectory()
        if d: self.install_path.set(d)

    def log(self, msg, color="white"):
        self.console.config(state='normal')
        tag = None
        if color == "green": tag = "green"
        if color == "red": tag = "red"
        if color == "warn": tag = "warn"
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        self.console.insert("end", f"[{ts}] {msg}\n", tag)
        self.console.see("end")
        self.console.config(state='disabled')
        self.update()

    def confirm_and_run(self):
        name = self.company_name.get().strip()
        if not name:
            self.log("ERROR: Organization Name Required", "red")
            return
            
        target_dir = Path(self.install_path.get()) / f"{name}-root"
        
        if target_dir.exists():
            resp = messagebox.askyesno("WARNING: Overwrite Detected", 
                f"The folder '{name}-root' already exists at this location.\n\n"
                "Continuing may OVERWRITE existing configuration files.\n"
                "Are you sure you want to proceed?")
            if not resp:
                self.log("Operation Cancelled by User", "warn")
                return
            else:
                self.log("User authorized overwrite.", "warn")

        self.log(f"Starting initialization for: {name}", "white")
        self.btn_run.config(text="DEPLOYING...", bg=COLOR_BRAND_MAIN)
        
        t = threading.Thread(target=self.execute_logic)
        t.daemon = True
        t.start()
        
        self.animate_progress(0, 100)

    def animate_progress(self, current, target):
        if current < target:
            step = max(1, (target - current) / 10)
            new_val = current + step
            width = self.progress_canvas.winfo_width()
            fill_width = (new_val / 100) * width
            self.progress_canvas.coords(self.progress_bar, 0, 0, fill_width, 4)
            self.after(20, lambda: self.animate_progress(new_val, target))
        else:
            self.btn_run.config(text="DEPLOY COMPLETE - SUCCESS", bg=COLOR_SUCCESS)

    def execute_logic(self):
        if CompanyStructureBuilder:
            try:
                root = Path(self.install_path.get()) / f"{self.company_name.get()}-root"
                builder = CompanyStructureBuilder(root, local_mode=True)
                
                builder.naming_rule = self.naming_rule.get()
                if builder.naming_rule == 'custom':
                    builder.naming_format = self.custom_format.get()
                
                original_create = builder.create_folder
                def verbose_create(p):
                    if p.exists():
                        self.log(f"Exists: {p.name} (Skipping)", "warn")
                    else:
                        self.log(f"Create: {p.name}", "white")
                    return original_create(p)
                builder.create_folder = verbose_create
                
                srv = [k for k,v in self.services.items() if v.get()]
                builder.build_complete_structure(selected_services=srv)
                
                self.log("-" * 20)
                self.log("DEPLOYMENT SUCCESSFUL", "green")
                self.log(f"Target: {root}", "green")
                self.installed_path = root
                
            except Exception as e:
                self.log(f"Backend Error: {e}", "red")
        else:
            self.log("ERROR: Backend module not found", "red")

if __name__ == "__main__":
    app = App()
    app.mainloop()
