from image_recognition.evaluator_manager import EvaluatorManager


def main():
    evaluator = EvaluatorManager()
    evaluator.network.model.summary()
    evaluator.network.model_compile()
    evaluator.network.model_fit()


if __name__ == '__main__':
    main()
