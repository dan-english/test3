from masoniteorm.migrations import Migration


class MessageCategoryTable(Migration):

    def up(self):

        with self.schema.create('message_category') as table:
          table.increments('id')
          table.string('account_id')
          table.string('message_id')
          table.string('category')
          table.string('model_version')
          table.string('categorized_at')

          table.timestamps()

    def down(self):
        self.schema.drop('message_category')

