<template>
  <CommonPage>
    <!-- 查询栏 -->
    <CrudTable ref="$table">
      <template #query-bar>
        <QueryBarItem>
          <NInput
            v-model="queryItems.appName"
            placeholder="请输入应用名称"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
      </template>
    </CrudTable>

    <!-- 新增/编辑 弹窗 -->
    <CrudModal
      v-model:visible="modalVisible"
      :title="modalTitle"
      :loading="modalLoading"
      @save="handleSave"
    >
      <NForm
        ref="modalFormRef"
        label-placement="left"
        label-align="left"
        :label-width="80"
        :model="modalForm"
        :rules="appRules"
      >
        <NFormItem label="应用名称" path="name">
          <NInput v-model:value="modalForm.name" clearable placeholder="请输入应用名称" />
        </NFormItem>
        <NFormItem label="应用描述" path="desc">
          <NInput v-model:value="modalForm.desc" type="textarea" clearable />
        </NFormItem>
        <NFormItem label="排序" path="order">
          <NInputNumber v-model:value="modalForm.order" min="0"></NInputNumber>
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>

<script setup>
import { h, onMounted, ref, resolveDirective, withDirectives } from 'vue'
import { NButton, NForm, NFormItem, NInput, NInputNumber, NPopconfirm, NTreeSelect } from 'naive-ui'

import CommonPage from '@/components/page/CommonPage.vue'
import QueryBarItem from '@/components/query-bar/QueryBarItem.vue'
import CrudModal from '@/components/table/CrudModal.vue'
import CrudTable from '@/components/table/CrudTable.vue'
import TheIcon from '@/components/icon/TheIcon.vue'

import { renderIcon } from '@/utils'
import { useCRUD } from '@/composables'
import api from '@/api'

defineOptions({ name: '应用管理' })

const $table = ref(null)
const queryItems = ref({ appName: '' })
const vPermission = resolveDirective('permission')

const {
  modalVisible,
  modalTitle,
  modalLoading,
  handleSave,
  modalForm,
  modalFormRef,
  handleEdit,
  handleDelete,
  handleAdd,
} = useCRUD({
  name: '应用',
  initForm: { order: 0 },
  doCreate: api.createApp,
  doUpdate: api.updateApp,
  doDelete: api.deleteApp,
  refresh: () => $table.value?.handleSearch(),
})

const appOption = ref([])
const isDisabled = ref(false)

onMounted(() => {
  $table.value?.handleSearch()
  api.getApps().then((res) => (appOption.value = res.data))
})

const appRules = {
  name: [
    {
      required: true,
      message: '请输入应用名称',
      trigger: ['input', 'blur', 'change'],
    },
  ],
}

async function addApps() {
  isDisabled.value = false
  handleAdd()
}

const columns = [
  {
    title: '应用名称',
    key: 'name',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '应用描述',
    key: 'desc',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '操作',
    key: 'actions',
    width: 'auto',
    align: 'center',
    fixed: 'right',
    render(row) {
      return [
        withDirectives(
          h(
            NButton,
            {
              size: 'small',
              type: 'primary',
              style: 'margin-left: 8px;',
              onClick: () => {
                handleEdit(row)
              },
            },
            {
              default: () => '编辑',
              icon: renderIcon('material-symbols:edit', { size: 16 }),
            }
          ),
          [[vPermission, 'post/api/v1/app/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ app_id: row.id }, false),
            onNegativeClick: () => {},
          },
          {
            trigger: () => h(
              NButton,
              {
                size: 'small',
                type: 'error',
                style: 'margin-left: 8px;',
              },
              {
                default: () => '删除',
                icon: renderIcon('material-symbols:delete', { size: 16 }),
              }
            )
          }
        )
      ]
    }
  }
]
</script>
