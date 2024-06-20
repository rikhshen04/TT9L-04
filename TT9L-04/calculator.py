import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pytesseract
from PIL import Image
import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas