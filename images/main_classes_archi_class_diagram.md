@startuml main_classes_archi_class_diagram
left to right direction
class Преподаватель
class Студент
class "Группа-дисциплина"

Преподаватель "*" --> "*" "Группа-дисциплина": преподаёт Д у Г
Студент "*" --> "*" "Группа-дисциплина": изучает Д в Г

@enduml