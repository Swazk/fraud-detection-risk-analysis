from src.run_model import load_data, preprocess, train_model, evaluate_model
import os, sys

def main():
    os.makedirs("results", exist_ok=True)
    try:
        df = load_data("data/creditcard.csv")
    except FileNotFoundError as e:
        print(e)
        print("If you want to download automatically, see the README for Kaggle steps.")
        sys.exit(1)

    X, y, scaler = preprocess(df)
    model, X_test, y_test = train_model(X, y)
    metrics = evaluate_model(model, X_test, y_test, results_dir="results")

    # Write summary markdown
    with open("fraud_analysis_summary.md", "w", encoding="utf8") as f:
        f.write("# Fraud Detection Summary\n\n")
        f.write(f"**Accuracy:** {metrics['accuracy']:.4f}\n\n")
        f.write("**Classification Report:**\n\n")
        f.write(metrics["report"])
        f.write("\n\n**Confusion Matrix:**\n")
        f.write(str(metrics["confusion_matrix"]) + "\n")

    print("Done. Results saved in the results/ folder and fraud_analysis_summary.md")

if __name__ == '__main__':
    main()
