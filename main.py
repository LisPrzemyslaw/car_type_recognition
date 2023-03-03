from image_recognition.evaluator_manager import EvaluatorManager
import matplotlib.pyplot as plt


def show_plot(history):
    print(f"{type(history)=}")
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Valid'], loc='upper left')
    plt.show()


def main():
    evaluator = EvaluatorManager()
    evaluator.network.model.summary()
    evaluator.network.model_compile()
    history = evaluator.network.model_fit()
    show_plot(history)


if __name__ == '__main__':
    main()
