from masoniteorm.migrations import Migration

class CreateDealsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """

        with self.schema.create('deals') as table:
          table.increments('id')
          table.string('title').default(' ')
          table.string('description').default(' ')
          table.string('organisation').default(' ')
          table.string('contact').default(' ')
          table.string('owner').default(' ')
          table.string('stage').default(' ')
          table.boolean('won').default(0)

          table.string('value').default('')

          table.timestamp('estimated_close_date').nullable()

          table.integer('user_id').unsigned()
          table.foreign('user_id').references('id').on('users')

          table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('deals')

