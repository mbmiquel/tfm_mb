import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def first_plot(y_test, y_pred):
    #Original vs. Predicción (Precio)
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, color='blue', label='Original vs. Predicción', alpha=0.7)
    plt.plot([0, max(y_test)], 
             [0, max(y_test)], 
             color='red', linestyle='--', label='Predicción perfecta')
        plt.title('Original vs. Predicción (Precio)')
    plt.xlabel('Original')
    plt.ylabel('Predicción')
    plt.legend()
    plt.grid(True)
    # Show the plot
    plt.show()

def second_plot(df_plot_diff):
    #Precio original vs. Error absoluto medio de la predicción
    plt.figure(figsize=(8, 6))
    df_plot_diff_sorted = df_plot_diff.sort_values(by="Original")
    plt.plot(
        df_plot_diff_sorted["Original"], 
        df_plot_diff_sorted["AbsDiff"], 
        color='blue', 
        alpha=0.7
    )
    plt.xscale('log')
    plt.title('Precio original vs. Error absoluto medio de la predicción')
    plt.xlabel('Precio original (log)')
    plt.ylabel('Error absoluto medio de la predicción')
    plt.legend()
    plt.grid(True)
    plt.show()

def third_plot(df_plot_diff_per):    
    #Precio original vs. % medio de error en la predicción
    plt.figure(figsize=(8, 6))
    df_plot_diff_per = df_plot_diff_per.sort_values(by="Original")
    plt.plot(
        df_plot_diff_per["Original"], 
        df_plot_diff_per["%error"], 
        color='blue', 
        alpha=0.7
    )
    plt.xscale('log')
    plt.title('Precio original vs. % medio de error en la predicción')
    plt.xlabel('Precio original (log)')
    plt.ylabel('% medio de error en la predicción')
    plt.legend()
    plt.grid(True)
    plt.show()

def forth_plot(df_plot):
    #Precio original vs. % medio de error en la predicción (intervalos logarítmicos)
    min_val = df_plot["Original"].min()
    max_val = df_plot["Original"].max()
    bins = np.logspace(np.log10(min_val), np.log10(max_val), num=500)  # Adjust 'num' for the number of bins
    df_plot["log_bin"] = pd.cut(df_plot["Original"], bins=bins, labels=bins[:-1])
    result = df_plot.groupby("log_bin")["%error"].mean().reset_index()
    result.rename(columns={"log_bin": "Original (Logarithmic Bins)", "%error": "Mean % Error"}, inplace=True)
    result=result.dropna()

    plt.figure(figsize=(8, 6))
    result = result.sort_values(by="Original (Logarithmic Bins)")
    plt.plot(
        result["Original (Logarithmic Bins)"], 
        result["Mean % Error"], 
        color='blue', 
        label='Predictions vs. Actual', 
        alpha=0.7
    )
    plt.xscale('log')
    plt.title('Precio original vs. % medio de error en la predicción (intervalos logarítmicos)')
    plt.xlabel('Precio original (log)')
    plt.ylabel('% medio de error en la predicción')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_performance(y_test, y_pred):
    #Original vs. Predicción
    first_plot(y_test, y_pred)

    df_plot = pd.DataFrame()
    df_plot["Original"] = y_test
    df_plot["Predicted"] = y_pred
    df_plot["AbsDiff"] = (df_plot["Original"]-df_plot["Predicted"]).abs()
    df_plot["%error"] = 100*df_plot["AbsDiff"]/df_plot["Original"]
    df_plot_diff = df_plot.groupby("Original")["AbsDiff"].mean().reset_index()
    df_plot_diff_per = df_plot.groupby("Original")["%error"].mean().reset_index()

    #Precio original vs. Error absoluto de la predicción
    second_plot(df_plot_diff)

    #Precio original vs. % de error en la predicción
    third_plot(df_plot_diff_per)

    # Precio original vs. % de error en la predicción (logaritmic bins)
    forth_plot(df_plot)
    
    
def fith_plot(y_test_base, y_pred_base, y_test_micro, y_pred_micro):
    #Precio original vs. % medio de error en la predicción (intervalos logarítmicos)
    df_plot_base = pd.DataFrame()
    df_plot_base["Original"] = y_test_base
    df_plot_base["Predicted"] = y_pred_base
    df_plot_base["AbsDiff"] = (df_plot_base["Original"]-df_plot_base["Predicted"]).abs()
    df_plot_base["%error"] = 100*df_plot_base["AbsDiff"]/df_plot_base["Original"]
    
    df_plot__micro = pd.DataFrame()
    df_plot__micro["Original"] = y_test_micro
    df_plot__micro["Predicted"] = y_pred_micro
    df_plot__micro["AbsDiff"] = (df_plot__micro["Original"]-df_plot__micro["Predicted"]).abs()
    df_plot__micro["%error"] = 100*df_plot__micro["AbsDiff"]/df_plot__micro["Original"]

    min_val = min(df_plot_base["Original"].min(), df_plot__micro["Original"].min())
    max_val = max(df_plot_base["Original"].max(), df_plot__micro["Original"].max())
    bins = np.logspace(np.log10(min_val), np.log10(max_val), num=500) 
    
    df_plot_base["log_bin"] = pd.cut(df_plot_base["Original"], bins=bins, labels=bins[:-1])
    result_blue = df_plot_base.groupby("log_bin")["%error"].mean().reset_index()
    result_blue.rename(columns={"log_bin": "Original (Logarithmic Bins)", "%error": "Mean % Error"}, inplace=True)
    result_blue = result_blue.dropna()
    result_blue = result_blue.sort_values(by="Original (Logarithmic Bins)")

    df_plot__micro["log_bin"] = pd.cut(df_plot__micro["Original"], bins=bins, labels=bins[:-1])
    result_red = df_plot__micro.groupby("log_bin")["%error"].mean().reset_index()
    result_red.rename(columns={"log_bin": "Original (Logarithmic Bins)", "%error": "Mean % Error"}, inplace=True)
    result_red = result_red.dropna()
    result_red = result_red.sort_values(by="Original (Logarithmic Bins)")

    plt.figure(figsize=(8, 6))

    # 1r DataFrame en azul
    plt.plot(
        result_blue["Original (Logarithmic Bins)"], 
        result_blue["Mean % Error"], 
        color='blue', 
        label='Original', 
        alpha=0.7
    )
    
    # 2n DataFrame en rojo
    plt.plot(
        result_red["Original (Logarithmic Bins)"], 
        result_red["Mean % Error"], 
        color='red', 
        label='Enriquecido', 
        alpha=0.7
    )
    
    plt.xscale('log')
    plt.title('Precio original vs. % medio de error en la predicción (intervalos logarítmicos)')
    plt.xlabel('Precio original (log)')
    plt.ylabel('% medio de error en la predicción')
    plt.legend()
    plt.grid(True)
    plt.show()
    