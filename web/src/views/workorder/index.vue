<template>
    <AppPage>
      <h1>工单列表</h1>
      <!-- 这里可以添加工单列表的表格组件 -->
      <CrudTable>
        <template #query>
          <QueryBar>
            <QueryBarItem>
              <NInput
                v-model:value="searchKeyword"
                placeholder="请输入工单名称"
                @keypress.enter="$table?.handleSearch()"
              />
            </QueryBarItem>
          </QueryBar>
        </template>
      </CrudTable>

      <!-- 新增/编辑 工单弹窗 -->
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
          :rules="workorderRules"
        >
          <NFormItem label="工单名称" path="name">
            <NInput v-model:value="modalForm.name" clearable placeholder="请输入工单名称" />
          </NFormItem>
          <NFormItem label="工单描述" path="desc">
            <NInput v-model:value="modalForm.desc" type="textarea" clearable />
          </NFormItem>
        </NForm>
      </CrudModal>
    </AppPage>
</template>

<script setup>
import { ref } from 'vue';

// 搜索关键词
const searchKeyword = ref('');
// 弹窗是否可见
const modalVisible = ref(false);
// 弹窗标题
const modalTitle = ref('');
// 弹窗加载状态
const modalLoading = ref(false);
// 表单引用
const modalFormRef = ref(null);
// 表单数据
const modalForm = ref({
  name: '',
  desc: ''
});
// 表单验证规则
const workorderRules = {
  name: {
    required: true,
    message: '请输入工单名称',
    trigger: 'blur'
  }
};

// 保存工单信息
const handleSave = () => {
  console.log('保存工单信息:', modalForm.value);
  modalVisible.value = false;
};
</script>
