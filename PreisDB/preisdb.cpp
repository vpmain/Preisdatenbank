#include "preisdb.h"
#include "ui_preisdb.h"

PreisDB::PreisDB(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::PreisDB)
{
    ui->setupUi(this);
}

PreisDB::~PreisDB()
{
    delete ui;
}

