#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "content.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_addKeyPushButton_clicked();

    void on_addDirPushButton_clicked();

    void on_searchPushButton_clicked();

private:
    Ui::MainWindow *ui;

    Content cnt;
};

#endif // MAINWINDOW_H
