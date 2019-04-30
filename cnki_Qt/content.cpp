#include "content.h"
#include <QtDebug>
#include <QFile>
Content::Content()
{

}

void Content::addKeyword(QString keyword)
{
    m_keywords.append(keyword);
}

void Content::addDir(QString dir)
{
    m_dirs.append(dir);
}

bool Content::saveToText()
{

    QString info;
    for (int i=0;i<m_dirs.size();i++) {
        //qDebug()<<m_dirs.at(i);
        if (i!=0)
            info += ',';
        info += m_dirs.at(i);
    }
    info += ';';
    for (int i=0;i<m_keywords.size();i++) {
        //qDebug()<<m_keywords.at(i);
        if (i!=0)
            info += ',';
        info += m_keywords.at(i);
    }
    info.replace("/","\\");
    qDebug()<<info;

    QFile file("search.config");
    if(file.exists())
        QFile::remove("search.config");

    file.open(QIODevice::ReadWrite | QIODevice::Text);
    QByteArray str = info.toUtf8();
    file.write(str);
    file.close();
    return true;
}
