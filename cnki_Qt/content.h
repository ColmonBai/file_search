#ifndef CONTENT_H
#define CONTENT_H
#include <QStringList>

class Content
{
public:
    Content();
    void addKeyword(QString keyword);
    void addDir(QString dir);
    bool saveToText();
private:
    QStringList m_dirs;
    QStringList m_keywords;
};

#endif // CONTENT_H
