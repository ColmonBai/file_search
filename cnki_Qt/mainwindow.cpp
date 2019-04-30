#include "mainwindow.h"
#include "ui_mainwindow.h"

#include "content.h"
#include <QtDebug>
#include <QMessageBox>
#include "QFileDialog"
#include "QDebug"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_addKeyPushButton_clicked()
{
    QString key = ui->inputLineEdit->text();
    if (key.isEmpty())
    {
        QMessageBox::warning(this, "warring", "请输入关键字");
            return;
    }
    cnt.addKeyword(key);
    QListWidgetItem *item = new QListWidgetItem;
    item->setText(key);
    ui->keyListWidget->addItem(item);
}

void MainWindow::on_addDirPushButton_clicked()
{
    QString file_name = QFileDialog::getExistingDirectory(this,"caption",".");
    //qDebug() << file_name;
    cnt.addDir(file_name);
    QListWidgetItem *item = new QListWidgetItem;
    item->setText(file_name);
    ui->dirListWidget->addItem(item);
}

void MainWindow::on_searchPushButton_clicked()
{
    if(cnt.saveToText()){
        system("main.exe");
    }
}
