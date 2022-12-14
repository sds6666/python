from tron_py.common.model import Model


class Version(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "version"
        self.table()

    # 更新数据的任务id
    def update_task_id(self, original_id, new_task_id):
        data = {
            "task_id": new_task_id
        }
        return self.where('task_id', '=', original_id).update(data)
