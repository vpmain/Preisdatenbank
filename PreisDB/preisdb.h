#ifndef PREISDB_H
#define PREISDB_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class PreisDB; }
QT_END_NAMESPACE

class PreisDB : public QMainWindow
{
    Q_OBJECT

public:
    PreisDB(QWidget *parent = nullptr);
    ~PreisDB();

private:
    Ui::PreisDB *ui;
};
#endif // PREISDB_H
