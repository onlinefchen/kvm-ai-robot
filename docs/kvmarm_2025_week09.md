# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 08:20:24

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 280
- **总 Thread 数**: 33
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 28 threads (261 邮件)
- **RFC**: 1 threads (2 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 1 threads (3 邮件)
- **Other**: 2 threads (12 邮件)

---

## 📌 PATCH

共 28 个 thread

---

### Thread 1: [PATCH v2 0/4] Selftest for pKVM ownership transitions

**📧 邮件数**: 28 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 25 Feb 2025 01:53:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 所做的自测补丁（PATCH v2 0/4），主要集中在内核虚拟化的内存所有权转换的自测功能上。

1. **原始补丁内容**：该补丁旨在为 pKVM 的内存所有权转换提供自测功能，包含对非保护型（NP）客户机的支持，并引入了新的数据段以支持非零全局变量的使用。

2. **之前讨论要点**：在之前的讨论中，参与者对补丁的功能进行了审查，提出了对错误处理的改进建议，尤其是去掉了不必要的警告（WARN），以便于测试。此外，补丁还更新了对内存转换的断言，以确保更好的测试覆盖。

3. **本周的新讨论和进展**：本周的讨论集中在补丁的具体实现上，参与者对补丁的各个部分进行了详细审查，提出了关于错误代码处理、内存映射及测试的具体建议。特别是，讨论了如何在不影响现有功能的情况下，优化 pKVM 的虚拟 CPU 创建过程。此外，关于 FF-A（Firmware Framework for Arm）缓冲区的初始化和管理也进行了相关讨论，确保其在保护模式下的正确性和稳定性。

总的来说，本周的讨论推动了补丁的进一步完善，确保了 pKVM 的自测功能能够有效地捕捉内存所有权转换中的潜在问题。

#### 📝 邮件列表

1. **[02-25 01:53]** [PATCH v2 0/4] Selftest for pKVM ownership transitions
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-25 01:53]** [PATCH v2 1/4] KVM: arm64: Add .hyp.data section
   - 发件人: Quentin Perret <qperret@google.com>
3. **[02-25 01:53]** [PATCH v2 2/4] KVM: arm64: Don't WARN from __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
4. **[02-25 01:53]** [PATCH v2 3/4] KVM: arm64: Selftest for pKVM transitions
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-25 01:53]** [PATCH v2 4/4] KVM: arm64: Extend pKVM selftest for np-guests
   - 发件人: Quentin Perret <qperret@google.com>
6. **[02-25 18:02]** Re: [PATCH v2 2/4] KVM: arm64: Don't WARN from __pkvm_host_share_guest()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-25 19:49]** Re: [PATCH v2 2/4] KVM: arm64: Don't WARN from
 __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
8. **[02-26 14:21]** Re: [PATCH v2 2/4] KVM: arm64: Don't WARN from __pkvm_host_share_guest()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-26 14:32]** Re: [PATCH v2 3/4] KVM: arm64: Selftest for pKVM transitions
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-26 18:10]** Re: [PATCH v2 3/4] KVM: arm64: Selftest for pKVM transitions
   - 发件人: Quentin Perret <qperret@google.com>
11. **[02-26 21:55]** [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[02-26 21:55]** [PATCH v2 1/4] KVM: arm64: Factor out setting HCRX_EL2 traps into
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[02-26 21:55]** [PATCH v2 2/4] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[02-26 21:55]** [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[02-26 21:55]** [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[02-27 12:09]** Re: [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its corresponding host vcpu
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-27 04:47]** Re: [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[02-27 14:13]** Re: [PATCH v2 4/4] KVM: arm64: Create each pKVM hyp vcpu after its corresponding host vcpu
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[02-27 14:13]** Re: [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[02-27 18:17]** [PATCH v2 0/4] KVM: arm64: Separate the hyp FF-A buffers init from
 the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
21. **[02-27 18:17]** [PATCH v2 1/4] KVM: arm64: Use the static initializer for the vesion lock
   - 发件人: Sebastian Ene <sebastianene@google.com>
22. **[02-27 18:17]** [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the
 ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
23. **[02-27 18:17]** [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
24. **[02-27 18:17]** [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx buffer
 to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
25. **[02-27 20:25]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
26. **[02-27 23:12]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
27. **[02-28 10:09]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the ffa header
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[02-28 19:44]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 2: [PATCH 0/7] KVM: x86: nVMX IRQ fix and VM teardown cleanups

**📧 邮件数**: 21 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 24 Feb 2025 15:55:35 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的一系列补丁，主要集中在 nVMX 中断修复和虚拟机拆解的清理工作上。

1. **原始补丁内容**：该补丁系列共有七个补丁，旨在修复 nVMX 中 KVM 无法检测到 L1 有待处理中断的问题，并对 x86 的虚拟机拆解流程进行清理。补丁 1 解决了在强制 VM-Exit 时可能导致空指针解引用的问题，补丁 2 则是针对 nVMX 的原始修复。

2. **之前讨论要点**：历史讨论中提到，x86 的嵌套拆解流程存在混乱，导致简单的修复变得复杂。补丁系列的目标是清理这些冗余的代码和逻辑，以提高代码的可维护性和稳定性。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现和逻辑上。参与者对补丁的顺序、必要性和潜在的改进提出了建议。例如，Yan Zhao 提出了对某些检查的合理性和冗余性的质疑，并建议在补丁中进行进一步的清理。此外，Sean Christopherson 表示已经将补丁 1 和 2 应用到主分支，并计划在后续版本中添加更多清理补丁。

总体而言，本周的讨论推动了补丁的进一步完善，并为未来的版本更新奠定了基础。

#### 📝 邮件列表

1. **[02-24 15:55]** [PATCH 0/7] KVM: x86: nVMX IRQ fix and VM teardown cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[02-24 15:55]** [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[02-24 15:55]** [PATCH 2/7] KVM: nVMX: Process events on nested VM-Exit if injectable
 IRQ or NMI is pending
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[02-24 15:55]** [PATCH 3/7] KVM: Assert that a destroyed/freed vCPU is no longer visible
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[02-24 15:55]** [PATCH 4/7] KVM: x86: Don't load/put vCPU when unloading its MMU
 during teardown
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[02-24 15:55]** [PATCH 5/7] KVM: x86: Unload MMUs during vCPU destruction, not before
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[02-24 15:55]** [PATCH 6/7] KVM: x86: Fold guts of kvm_arch_sync_events() into kvm_arch_pre_destroy_vm()
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[02-24 15:55]** [PATCH 7/7] KVM: Drop kvm_arch_sync_events() now that all
 implementations are nops
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[02-25 15:07]** Re: [PATCH 3/7] KVM: Assert that a destroyed/freed vCPU is no longer
 visible
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
10. **[02-25 15:13]** Re: [PATCH 4/7] KVM: x86: Don't load/put vCPU when unloading its MMU
 during teardown
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
11. **[02-25 15:44]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
12. **[02-25 20:05]** Re: [PATCH 7/7] KVM: Drop kvm_arch_sync_events() now that all
 implementations are nops
   - 发件人: bibo mao <maobibo@loongson.cn>
13. **[02-25 06:35]** Re: [PATCH 3/7] KVM: Assert that a destroyed/freed vCPU is no longer visible
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[02-25 06:44]** Re: [PATCH 4/7] KVM: x86: Don't load/put vCPU when unloading its MMU
 during teardown
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[02-25 07:04]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[02-25 17:15]** Re: [PATCH 7/7] KVM: Drop kvm_arch_sync_events() now that all
 implementations are nops
   - 发件人: Claudio Imbrenda <imbrenda@linux.ibm.com>
17. **[02-26 00:47]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
18. **[02-25 16:27]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[02-26 15:34]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
20. **[02-26 10:18]** Re: [PATCH 1/7] KVM: x86: Free vCPUs before freeing VM state
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
21. **[02-26 19:38]** Re: [PATCH 0/7] KVM: x86: nVMX IRQ fix and VM teardown cleanups
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 3: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 20 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 18 Feb 2025 14:39:55 -0600

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 arm64 架构上启用分支栈采样的补丁（PATCH v20 00/11）。该补丁系列的主要目的是通过 ARMv9.2 架构特性“分支记录缓冲扩展”（BRBE）来支持性能监控（perf）中的分支栈采样。

在历史讨论中，Rob Herring 介绍了该补丁的背景，并指出补丁的前七个部分是清理和准备工作，后四个部分则是具体实现。特别是第10和第11个补丁涉及在 nVHE（非虚拟化高效）环境中禁用访客的分支生成，以及为 BRBE 添加支持。

在本周的新讨论中，参与者们对补丁进行了审查和反馈。Leo Yan 提出了对任务迁移时分支记录保存和恢复的担忧，认为当前实现仅在任务调度时无条件失效所有记录，可能导致用户空间跟踪不完整。Mark Rutland 和 Rob Herring 对此进行了回应，讨论了在事件轮换和上下文切换时如何处理分支记录的问题，认为在某些情况下丢失记录是可以接受的。

最终，Rob Herring 确认了一些清理工作已被应用，并感谢参与者的贡献。整体来看，讨论集中在如何优化 BRBE 的实现以提高性能监控的准确性和有效性。

#### 📝 邮件列表

1. **[02-18 14:39]** [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[02-18 14:40]** [PATCH v20 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[02-18 14:40]** [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
4. **[02-24 10:41]** Re: [PATCH v20 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[02-24 12:25]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
6. **[02-24 06:46]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
7. **[02-24 14:03]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
8. **[02-24 16:05]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[02-24 18:03]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
10. **[02-24 19:31]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
11. **[02-25 12:01]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
12. **[02-25 12:38]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
13. **[02-25 09:35]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
14. **[02-25 17:48]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
15. **[02-25 13:04]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
16. **[02-25 19:46]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
17. **[02-25 19:58]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Mark Rutland <mark.rutland@arm.com>
18. **[02-26 13:48]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Leo Yan <leo.yan@arm.com>
19. **[02-26 08:26]** Re: [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
20. **[03-01 07:05]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 4: [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 10:25:16 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM np-guest 的阶段二（Stage-2）巨大映射（huge mappings）支持的补丁系列（共9个补丁）。这些补丁旨在为 pKVM np-guest 安装 PMD 级别的映射，特别是在 Stage-1 被 Hugetlbfs 或 THP（透明大页）支持时。

**补丁内容**：
- 第一个补丁（PATCH 1/9）处理了 np-guest 的巨大映射，修改了缓存操作以支持大于 PAGE_SIZE 的大小。
- 后续补丁逐步添加了对不同 hypercall 的支持，包括共享、取消共享、写保护和清除年轻页的功能，均支持 nr_pages 参数，以便处理 PMD_SIZE 的映射。

**历史讨论要点**：
- 之前的讨论集中在如何优化对巨大映射的支持，确保在处理不同大小的映射时，系统的稳定性和性能不会受到影响。

**本周新讨论与进展**：
- 本周的讨论主要集中在补丁的实现细节和潜在的安全性问题上，参与者对代码的健壮性提出了疑虑，特别是在处理非页面对齐的大小时。Vincent Donnefort 和 Quentin Perret 之间的交流强调了确保物理地址有效性的重要性，以避免潜在的内存访问错误。

总的来说，此次讨论推动了对 pKVM np-guest 支持巨大映射的实现，确保了系统在处理大页时的效率和安全性。

#### 📝 邮件列表

1. **[02-28 10:25]** [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-28 10:25]** [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-28 10:25]** [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-28 10:25]** [PATCH 2/9] KVM: arm64: Add range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[02-28 10:25]** [PATCH 3/9] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[02-28 10:25]** [PATCH 3/9] KVM: arm64: Add range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[02-28 10:25]** [PATCH 4/9] KVM: arm64: Add a range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[02-28 10:25]** [PATCH 4/9] KVM: arm64: Add range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[02-28 10:25]** [PATCH 5/9] KVM: arm64: Add a range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[02-28 10:25]** [PATCH 5/9] KVM: arm64: Add range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[02-28 10:25]** [PATCH 6/9] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[02-28 10:25]** [PATCH 7/9] KVM: arm64: Add a range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[02-28 10:25]** [PATCH 7/9] KVM: arm64: Add range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[02-28 10:25]** [PATCH 8/9] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[02-28 10:25]** [PATCH 9/9] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[02-28 18:54]** Re: [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Quentin Perret <qperret@google.com>
17. **[02-28 19:06]** Re: [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 5: [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support

**📧 邮件数**: 17 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 25 Feb 2025 17:29:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加 NV GICv3 支持的补丁（PATCH v4 00/16）。该补丁旨在增强 KVM 的虚拟化能力，特别是在处理 GICv3 中断控制器时。

在历史讨论中，Marc Zyngier 提到该补丁的多个版本（v1 到 v4），每个版本都进行了相应的修改和优化。例如，v1 修复了 MI INTID 的默认值，v2 和 v3 则进行了重基于内核版本的更新，并加入了来自 Andre 的代码审查反馈。

本周的新讨论中，Marc Zyngier 提交了多个补丁，主要包括：
1. **补丁 1**：添加 ICH_HCR_EL2 的布局，确保对控制位的正确描述。
2. **补丁 2-4**：添加 ICH_VTR_EL2 和 ICH_MISR_EL2 的布局，并确保在加载 GIC 之前先加载定时器，以解决中断注入时的状态问题。
3. **补丁 5-15**：涉及对 GICv3 EL2 访问的处理、维护中断的仿真、L2 到 L1 的中断注入处理等，确保在嵌套虚拟化环境中正确管理中断状态和上下文。

最后，补丁 16 强调了在没有 GICv3 的情况下，KVM 初始化应失败，以确保硬件兼容性。

总体来看，本周的讨论集中在完善 GICv3 支持的细节上，确保 KVM 在嵌套虚拟化场景下的稳定性和功能性。

#### 📝 邮件列表

1. **[02-25 17:29]** [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-25 17:29]** [PATCH v4 01/16] arm64: sysreg: Add layout for ICH_HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-25 17:29]** [PATCH v4 02/16] arm64: sysreg: Add layout for ICH_VTR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-25 17:29]** [PATCH v4 03/16] arm64: sysreg: Add layout for ICH_MISR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-25 17:29]** [PATCH v4 04/16] KVM: arm64: nv: Load timer before the GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-25 17:29]** [PATCH v4 05/16] KVM: arm64: nv: Add ICH_*_EL2 registers to vpcu_sysreg
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-25 17:29]** [PATCH v4 06/16] KVM: arm64: nv: Plumb handling of GICv3 EL2 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-25 17:29]** [PATCH v4 07/16] KVM: arm64: nv: Sanitise ICH_HCR_EL2 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-25 17:29]** [PATCH v4 08/16] KVM: arm64: nv: Nested GICv3 emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-25 17:29]** [PATCH v4 09/16] KVM: arm64: nv: Handle L2->L1 transition on interrupt injection
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-25 17:29]** [PATCH v4 10/16] KVM: arm64: nv: Add Maintenance Interrupt emulation
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[02-25 17:29]** [PATCH v4 11/16] KVM: arm64: nv: Respect virtual HCR_EL2.TWx setting
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[02-25 17:29]** [PATCH v4 12/16] KVM: arm64: nv: Request vPE doorbell upon nested ERET to L2
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[02-25 17:29]** [PATCH v4 13/16] KVM: arm64: nv: Propagate used_lrs between L1 and L0 contexts
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[02-25 17:29]** [PATCH v4 14/16] KVM: arm64: nv: Fold GICv3 host trapping requirements into guest setup
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-25 17:29]** [PATCH v4 15/16] KVM: arm64: nv: Allow userland to set VGIC maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-25 17:29]** [PATCH v4 16/16] KVM: arm64: nv: Fail KVM init if asking for NV without GICv3
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH 0/4] mm: Rework generic PTDUMP configs

**📧 邮件数**: 16 | **👥 参与者**: 5 | **📅 开始时间**: Thu, 13 Feb 2025 09:39:30 +0530

#### 🤖 AI 总结

本邮件线程讨论了两个主要主题：一是针对 Linux 内核中 PTDUMP 配置的重构补丁，二是 KVM 在 arm64 平台上针对 GICv4 vLPI 注入的修复和澄清。

**历史讨论：**
Anshuman Khandual 提出了一个补丁系列，旨在重构通用 PTDUMP 配置，并在进行一些基本清理后对其进行重命名。补丁的目标是消除 GENERIC_PTDUMP 和 PTDUMP_CORE 之间的混淆，建议将其重命名为 ARCH_HAS_PTDUMP 和 PTDUMP，以提高可读性。参与者 Christophe Leroy 和 Steven Price 对命名的适当性进行了讨论，提出了不同的观点，认为当前的命名可能不够明确。

**本周新讨论：**
在本周的讨论中，Christophe Leroy 对补丁的命名提出了进一步的质疑，认为 CONFIG_ARCH_HAS_SOMETHING 的表述不够准确。Oliver Upton 则提交了一系列针对 KVM 的补丁，解决了 GICv4 vLPI 注入中的一些问题，包括限制对硬件 IRQ 不匹配的警告、在找不到 LPI 时回退到软件中断注入，以及文档化 IRQBYPASS 的恢复顺序要求。这些补丁得到了 Marc Zyngier 的认可，并已被应用于下一个版本中。

总体而言，本周的讨论集中在对补丁的细节和命名的澄清上，同时也推进了 KVM 相关问题的修复。

#### 📝 邮件列表

1. **[02-13 09:39]** [PATCH 0/4] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-13 09:39]** [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-13 08:38]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
4. **[02-13 11:23]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Steven Price <steven.price@arm.com>
5. **[02-13 12:49]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
6. **[02-14 12:47]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-14 12:56]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
8. **[02-24 12:12]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
9. **[02-24 12:13]** Re: [PATCH 4/4] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
10. **[02-26 10:31]** [PATCH 0/4] KVM: arm64: Fixes/clarification for GICv4 vLPI injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-26 10:31]** [PATCH 1/4] KVM: arm64: vgic-v4: Only attempt vLPI mapping for actual MSIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[02-26 10:31]** [PATCH 2/4] KVM: arm64: vgic-v4: Only WARN for HW IRQ mismatch when unmapping vLPI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[02-26 10:31]** [PATCH 3/4] KVM: arm64: vgic-v4: Fall back to software irqbypass if LPI not found
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[02-26 10:31]** [PATCH 4/4] KVM: arm64: Document ordering requirements for irqbypass
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[02-26 18:58]** Re: [PATCH 0/4] KVM: arm64: Fixes/clarification for GICv4 vLPI injection
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-26 13:27]** Re: [PATCH 0/4] KVM: arm64: Fixes/clarification for GICv4 vLPI injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation

**📧 邮件数**: 14 | **👥 参与者**: 6 | **📅 开始时间**: Mon, 24 Feb 2025 15:09:38 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）的补丁，主题为“在内存槽创建过程中去掉 mte_allowed 检查”。该补丁的目的是允许创建不带 VM_MTE_ALLOWED 标志的内存槽，从而解决用户在启用 MTE（内存标签扩展）时使用 VFIO（虚拟功能 I/O）直通的问题。

在历史讨论中，补丁的背景是由于之前的提交将内存槽的检查进行了统一，导致在某些情况下，内存槽被拒绝创建。之前的实现中，内存槽仅在 VM_SHARED 标志设置时被拒绝，而现在则是在 VM_MTE_ALLOWED 未设置的情况下也会被拒绝。补丁的提出是为了恢复到之前的行为，以支持 MTE 和 VFIO 的兼容性。

本周的新讨论中，参与者对补丁的内容进行了多次审议和测试。Suzuki K Poulose 表示已测试该补丁，Catalin Marinas 和 Marc Zyngier 提出了对补丁的理解和潜在问题，特别是关于 MTE 和 VFIO 之间的交互，以及如何确保虚拟机监控器（VMM）能够正确处理标签访问错误。Aneesh Kumar K.V 提出了改进建议，包括在内存故障时提供更多信息以帮助调试。

总体来看，补丁得到了积极的反馈，但仍需进一步讨论如何确保 VMM 和客体在 MTE 和内存映射方面的一致性和安全性。

#### 📝 邮件列表

1. **[02-24 15:09]** [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[02-24 10:32]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[02-24 11:05]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[02-24 12:24]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-24 14:39]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-24 15:02]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-24 22:14]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
8. **[02-24 17:23]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-24 18:00]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[02-26 00:02]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-26 15:28]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
12. **[02-26 15:58]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
13. **[02-26 22:18]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot creation
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
14. **[02-26 18:02]** Re: [PATCH] KVM: arm64: Drop mte_allowed check during memslot
 creation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 8: [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 24 Feb 2025 16:53:56 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现可写的 MIDR（主实现 ID 寄存器）、REVIDR（修订实现 ID 寄存器）和 AIDR（架构实现 ID 寄存器）的补丁系列。

1. **原始补丁内容**：
   本系列补丁的目标是使 MIDR、REVIDR 和 AIDR 寄存器可由用户空间修改，以便在虚拟机中提供一致的实现 ID 值。补丁还涉及到对这些寄存器的访问控制和状态管理。

2. **之前讨论要点**：
   在之前的讨论中，开发者们强调了现有实现的不足之处，尤其是如何在不破坏 ABI（应用二进制接口）的情况下实现可写寄存器。补丁的设计考虑了用户空间的参与，以确保在寄存器可写时，所有 vCPU 都能看到一致的值。

3. **本周新讨论与进展**：
   本周的讨论中，开发者们对补丁进行了细化和修改，确保在处理 SMIDR_EL1 访问时能够正确触发未定义异常，并且在用户空间要求下允许对实现 ID 寄存器的写入。补丁的多个版本（v1到v4）被提交，涉及对寄存器访问的改进和测试用例的添加。此外，Marc Zyngier 提出了对补丁的一些建议和改进意见，确保在处理 AArch32 版本的 REVIDR 和 AIDR 时的兼容性。最终，Oliver Upton 确认将这些补丁应用到下一个版本中。

整体来看，本周的讨论集中在补丁的细节调整和测试验证上，确保新功能的稳定性和兼容性。

#### 📝 邮件列表

1. **[02-24 16:53]** [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-24 16:53]** [PATCH v4 1/5] KVM: arm64: Set HCR_EL2.TID1 unconditionally
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-24 16:53]** [PATCH v4 2/5] KVM: arm64: Maintain per-VM copy of implementation ID regs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-24 16:53]** [PATCH v4 3/5] KVM: arm64: Load VPIDR_EL2 with the VM's MIDR_EL1 value
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-24 16:54]** [PATCH v4 4/5] KVM: arm64: Allow userspace to change the implementation ID registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[02-24 16:54]** [PATCH v4 5/5] KVM: selftests: arm64: Test writes to MIDR,REVIDR,AIDR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[02-25 11:09]** Re: [PATCH v4 1/5] KVM: arm64: Set HCR_EL2.TID1 unconditionally
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-25 11:19]** Re: [PATCH v4 4/5] KVM: arm64: Allow userspace to change the implementation ID registers
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-25 13:54]** Re: [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-26 01:49]** Re: [PATCH v4 0/5] KVM: arm64: Writable MIDR/REVIDR (and associated baggage)
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[02-27 20:39]** Re: [PATCH v4 5/5] KVM: selftests: arm64: Test writes to
 MIDR,REVIDR,AIDR
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[02-28 10:47]** Re: [PATCH v4 5/5] KVM: selftests: arm64: Test writes to
 MIDR,REVIDR,AIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
13. **[02-28 14:21]** Re: [PATCH v4 5/5] KVM: selftests: arm64: Test writes to
 MIDR,REVIDR,AIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 9: [PATCH V3 0/5] mm: Rework generic PTDUMP configs

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 26 Feb 2025 17:53:59 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是对 Linux 内核中通用 PTDUMP 配置的重构，包含五个补丁（PATCH V3 0/5）。补丁的主要目的是在进行一些基本清理后，重命名通用 PTDUMP 配置，以提高可读性和一致性。

在历史讨论中，补丁的背景是为了改善现有的 PTDUMP 配置，使其更符合不同平台的需求。之前的版本（V1 和 V2）中，Anshuman Khandual 提出了多项修改，包括删除不必要的配置选项和调整依赖关系。

本周的新讨论中，Anshuman Khandual 提交了 V3 版本的补丁，并详细列出了每个补丁的具体修改内容。主要变化包括：
1. 从 `debug.config` 中删除 `GENERIC_PTDUMP` 配置，以避免在不支持的平台上启用该选项。
2. 在 PowerPC 的配置中，将 `GENERIC_PTDUMP` 替换为 `CONFIG_PTDUMP_DEBUGFS`。
3. 更新文档，删除不再可选的 PTDUMP 配置选项。
4. 将 `DEBUG_WX` 的依赖关系改为依赖于 `GENERIC_PTDUMP`。
5. 重命名 `GENERIC_PTDUMP` 和 `PTDUMP_CORE` 为 `ARCH_HAS_PTDUMP` 和 `PTDUMP`，以增强配置的清晰度。

本周的讨论中，多个参与者对补丁进行了审查并表示支持，显示出对该改动的积极反馈。整体来看，此次讨论和补丁提交旨在提升内核配置的整洁性和可维护性。

#### 📝 邮件列表

1. **[02-26 17:53]** [PATCH V3 0/5] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-26 17:54]** [PATCH V3 1/5] configs: Drop GENERIC_PTDUMP from debug.config
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-26 17:54]** [PATCH V3 2/5] arch/powerpc: Drop GENERIC_PTDUMP from mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-26 17:54]** [PATCH V3 3/5] docs: arm64: Drop PTDUMP config options from ptdump.rst
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[02-26 17:54]** [PATCH V3 4/5] mm: Make DEBUG_WX depdendent on GENERIC_PTDUMP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[02-26 17:54]** [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-26 13:31]** Re: [PATCH V3 2/5] arch/powerpc: Drop GENERIC_PTDUMP from
 mpc885_ads_defconfig
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
8. **[02-26 13:31]** Re: [PATCH V3 4/5] mm: Make DEBUG_WX depdendent on GENERIC_PTDUMP
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
9. **[02-26 13:33]** Re: [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
10. **[02-26 19:45]** Re: [PATCH V3 3/5] docs: arm64: Drop PTDUMP config options from
 ptdump.rst
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[02-26 19:53]** Re: [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[02-27 05:36]** Re: [PATCH V3 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 10: [PATCH 00/11] Tracefs support for pKVM

**📧 邮件数**: 12 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 24 Feb 2025 12:13:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（共11个补丁），主要由 Vincent Donnefort 提出。该补丁旨在为保护模式下的虚拟化提供调试和性能分析工具，Tracefs 被认为是理想的选择，因为其易用性和广泛的工具支持。

**补丁内容**：
1. **补丁目的**：引入一种方法来创建和生成来自 hypervisor 的事件，并提供一个 Tracefs 用户空间接口以读取这些事件。
2. **补丁结构**：包括环形缓冲区的设置、Tracefs 接口的创建、事件的生成等。

**历史讨论要点**：
- 之前的讨论集中在如何实现 hypervisor 的事件追踪，强调了与内核的不同之处，如事件格式和环形缓冲区的操作。
- 讨论中提到的限制包括不支持非消耗性读取等。

**本周新讨论和进展**：
- 本周的讨论主要集中在补丁的具体实现细节上，包括环形缓冲区的远程写入、Tracefs 接口的扩展、时钟支持的引入等。
- 新增了对 hyp 事件的支持，允许在 hypervisor 中描述和发出事件，并为用户空间工具提供了直接读取环形缓冲区的原始接口。
- 还增加了自测试功能，以验证新引入的 Tracefs 接口的有效性。

总体而言，该系列补丁为 pKVM 提供了强大的调试和性能分析能力，促进了对 hypervisor 行为的深入理解。

#### 📝 邮件列表

1. **[02-24 12:13]** [PATCH 00/11] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-24 12:13]** [PATCH 01/11] ring-buffer: Introduce ring-buffer remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-24 12:13]** [PATCH 02/11] ring-buffer: Expose buffer_data_page material
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-24 12:13]** [PATCH 03/11] KVM: arm64: Support unaligned fixmap in the nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[02-24 12:13]** [PATCH 04/11] KVM: arm64: Add clock support in the nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[02-24 12:13]** [PATCH 05/11] KVM: arm64: Add tracing support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[02-24 12:13]** [PATCH 06/11] KVM: arm64: Add hyp tracing to tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[02-24 12:13]** [PATCH 07/11] KVM: arm64: Add clock for hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[02-24 12:13]** [PATCH 08/11] KVM: arm64: Add raw interface for hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[02-24 12:13]** [PATCH 09/11] KVM: arm64: Add trace interface for hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[02-24 12:13]** [PATCH 10/11] KVM: arm64: Add support for hyp events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[02-24 12:13]** [PATCH 11/11] KVM: arm64: Add kselftest for tracefs hyp tracefs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 11: [PATCH 0/2] KVM: arm64: PSCI relay fixes

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 18:05:24 +0000

#### 🤖 AI 总结

本邮件讨论主题为「KVM: arm64: PSCI relay 修复」，主要涉及两个补丁的提交和讨论。补丁旨在修复PSCI中缺失的初始化，防止在CPU_ON、CPU_SUSPEND和SYSTEM_SUSPEND等冷启动入口时导致主机内核崩溃。

历史讨论中，补丁的第一个部分由Mark Rutland提出，修复了HCR_EL2.E2H的初始化问题，确保在进入KVM时该寄存器能够可靠读取。第二部分由Ahmed Genidi提出，修复了SCTLR_EL1的初始化问题，以避免在进入EL1时出现未知状态，从而导致内核崩溃。

在本周的新讨论中，参与者对补丁进行了详细审查和讨论。Leo Yan提出了对HCR_EL2.E2H初始化代码的改进建议，Marc Zyngier则指出了代码逻辑中的错误，强调需要确保在特定情况下正确设置E2H位。最终，Mark Rutland确认了补丁的修复效果，并将其应用于代码库中。

总结而言，本周的讨论集中在对补丁的细节审查和逻辑修正上，确保了KVM在处理PSCI调用时的稳定性和可靠性。

#### 📝 邮件列表

1. **[02-27 18:05]** [PATCH 0/2] KVM: arm64: PSCI relay fixes
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[02-27 18:05]** [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[02-27 18:05]** [PATCH 2/2] KVM: arm64: Initialize SCTLR_EL1 in __kvm_hyp_init_cpu()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
4. **[02-28 09:29]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[02-28 09:43]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-28 09:52]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[02-28 09:56]** Re: [PATCH 2/2] KVM: arm64: Initialize SCTLR_EL1 in
 __kvm_hyp_init_cpu()
   - 发件人: Leo Yan <leo.yan@arm.com>
8. **[02-28 10:14]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Leo Yan <leo.yan@arm.com>
9. **[02-28 10:20]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-28 11:13]** Re: [PATCH 1/2] KVM: arm64: Initialize HCR_EL2.E2H early
   - 发件人: Mark Rutland <mark.rutland@arm.com>
11. **[03-02 08:41]** Re: [PATCH 0/2] KVM: arm64: PSCI relay fixes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 13 Feb 2025 16:13:40 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的补丁系列（PATCH v7 00/45）。该补丁旨在实现受保护虚拟机的运行，相关的来宾支持已在 v6.14-rc1 中合并。补丁的主要改动包括分离 RMM 粒度大小和 PAGE_SIZE 的概念，使得主机可以使用大于 4k 的 PAGE_SIZE。

在历史讨论中，补丁的多个部分被逐一介绍，包括对 KVM 处理共享映射的准备、修复构建错误、处理粒度保护故障以及为 RMM 调用添加 SMC 定义等。这些补丁经过了多次审查和修改，以确保功能的正确性和代码的整洁性。

在本周的新讨论中，Gavin Shan 对多个补丁进行了审查并给予了“Reviewed-by”的反馈。他指出了补丁 01 中的成员变量可能与之前的 attr_filter 重复，并确认了补丁 02、03 和 04 的审查意见。整体来看，本周的讨论主要集中在对补丁的审查和确认上，未出现新的问题或争议。

#### 📝 邮件列表

1. **[02-13 16:13]** [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[02-13 16:13]** [PATCH v7 01/45] KVM: Prepare for handling only shared mappings in mmu_notifier events
   - 发件人: Steven Price <steven.price@arm.com>
3. **[02-13 16:13]** [PATCH v7 02/45] kvm: arm64: Include kvm_emulate.h in kvm/arm_psci.h
   - 发件人: Steven Price <steven.price@arm.com>
4. **[02-13 16:13]** [PATCH v7 03/45] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
5. **[02-13 16:13]** [PATCH v7 04/45] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
6. **[03-03 09:36]** Re: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events
   - 发件人: Gavin Shan <gshan@redhat.com>
7. **[03-03 09:39]** Re: [PATCH v7 02/45] kvm: arm64: Include kvm_emulate.h in
 kvm/arm_psci.h
   - 发件人: Gavin Shan <gshan@redhat.com>
8. **[03-03 09:43]** Re: [PATCH v7 03/45] arm64: RME: Handle Granule Protection Faults
 (GPFs)
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[03-03 09:52]** Re: [PATCH v7 04/45] arm64: RME: Add SMC definitions for calling the
 RMM
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 13: [PATCH v1 0/3] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 14 Feb 2025 15:02:55 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要目的是修复 pKVM 中 HCRX_EL2 和其他陷阱的初始化问题。历史讨论中，Fuad Tabba 提出了一个补丁（PATCH v1 1/3），旨在确保当系统支持 HCRX_EL2 寄存器时，能够正确初始化和设置相关陷阱。该补丁的实现涉及在 pKVM 的代码中增加了 46 行新代码。

在之前的讨论中，参与者们关注了补丁的有效性和必要性，尤其是与 KVM 中的其他部分（如 kvm_calculate_traps()）保持一致性的重要性。

本周的新讨论中，Oliver Upton 和 Marc Zyngier 对补丁进行了进一步的审查和讨论。Oliver 提出可以去掉某些不再支持的功能，以简化代码。Marc 则建议将 HCRX 的初始化部分提取到一个共享的内联函数中，以便在多个地方调用。最终，Fuad 表示将根据讨论的反馈进行修改，确保补丁的有效性和一致性。整体来看，讨论集中在如何优化和清理代码，以提高 KVM 的稳定性和可维护性。

#### 📝 邮件列表

1. **[02-14 15:02]** [PATCH v1 0/3] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-14 15:02]** [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-26 02:07]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-26 10:45]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-26 04:36]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[02-26 04:44]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[02-26 15:28]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-26 10:53]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[02-26 10:54]** Re: [PATCH v1 1/3] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 14: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 19 Feb 2025 14:30:28 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构上为 Realms 启用内存加密的补丁（PATCH v7 09/11）。历史讨论中，Steven Price 提到，由于 RSI 检测的延迟，调用 is_realm_world() 的时机过早，可能导致某些 Realm 客户端无法与主机共享页面。他提出了两种解决方案，其中一种是将 rodata_full 设为 Realm 客户端的要求。

在本周的新讨论中，参与者们围绕如何处理 rodata_full 和页面映射的问题展开了深入的讨论。Catalin Marinas 和 Will Deacon 讨论了在不影响权限的情况下，是否可以在存在 RMM 时强制进行页面映射。Steven Price 提出了一个新的选项，即提供一个不同于 rodata_full 的编译/命令行标志，以允许在不影响权限的情况下支持 Realm。

总体来看，本周的讨论集中在如何平衡内存映射和权限设置之间的关系，以及如何在实现中避免复杂性的问题上。参与者们一致认为，长远来看，应该避免将实现细节暴露给用户，并考虑更清晰的解决方案。

#### 📝 邮件列表

1. **[02-19 14:30]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Steven Price <steven.price@arm.com>
2. **[02-26 19:03]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[02-27 00:23]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Will Deacon <will@kernel.org>
4. **[02-27 10:45]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Steven Price <steven.price@arm.com>
5. **[02-27 10:55]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-27 17:22]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Will Deacon <will@kernel.org>
7. **[02-27 21:21]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 15: [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 27 Feb 2025 00:33:04 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于将 pKVM 所有权状态迁移到 hyp_vmemmap 的补丁系列，共包含六个补丁。该补丁的主要目的是提高超管状态查找的效率，并简化未来功能的实现。

在历史讨论中，Quentin Perret 提到迁移的两个主要好处：首先，可以避免在查找超管状态时进行页面表遍历，从而降低开销；其次，超管状态与线性映射范围的存在解耦，使得现有代码的清理和未来特性（如超管追踪）的引入变得更加简单。

本周的新讨论中，Quentin 提交了六个补丁，具体内容如下：
1. **补丁 1**：确保在处理启用 SVE 的客户机时，主机的 SVE 状态在 EL2 S1 处被固定。
2. **补丁 2**：将 PKVM_NOPAGE 的编码改为使用保留状态，以简化后续迁移。
3. **补丁 3**：引入 {get,set}_host_state() 辅助函数，以便更好地访问主机状态。
4. **补丁 4**：将超管状态迁移到 hyp_vmemmap，以提高查找效率。
5. **补丁 5**：推迟在共享时的 EL2 stage-1 映射，以增强安全性。
6. **补丁 6**：在所有涉及超管的内存所有权转换中无条件交叉检查超管状态，避免潜在问题。

这些补丁的实施将显著改善超管的性能和安全性。

#### 📝 邮件列表

1. **[02-27 00:33]** [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-27 00:33]** [PATCH 1/6] KVM: arm64: Track SVE state in the hypervisor vcpu structure
   - 发件人: Quentin Perret <qperret@google.com>
3. **[02-27 00:33]** [PATCH 2/6] KVM: arm64: Use 0b11 for encoding PKVM_NOPAGE
   - 发件人: Quentin Perret <qperret@google.com>
4. **[02-27 00:33]** [PATCH 3/6] KVM: arm64: Introduce {get,set}_host_state() helpers
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-27 00:33]** [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
6. **[02-27 00:33]** [PATCH 5/6] KVM: arm64: Defer EL2 stage-1 mapping on share
   - 发件人: Quentin Perret <qperret@google.com>
7. **[02-27 00:33]** [PATCH 6/6] KVM: arm64: Unconditionally cross check hyp state
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 16: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 14:02:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的虚拟机实时迁移的错误管理的补丁集（PATCH v8 0/6）。该补丁集的主要目的是增强对目标 CPU 实现的支持，以便在虚拟机迁移过程中能够正确处理相关的错误。

在历史讨论中，Shameer Kolothum 提出了多个补丁，主要包括：
1. 修改 `_midr_range()` 函数以内部读取 MIDR/REVIDR，奠定支持来宾内核的基础。
2. 将 `_midr_in_range_list()` 函数导出，以便后续补丁能够访问新的数据。
3. 基于实现 CPU 启用错误管理，通过超调用获取迁移目标的实现 CPU。

本周的新讨论中，Catalin Marinas 对多个补丁进行了确认，表示认可（Acked-by），包括对补丁 1、4 和 5 的支持。他指出虽然存在潜在问题，但在没有更好方案的情况下，补丁是可行的。这表明补丁集在社区中获得了积极的反馈，并朝着合并的方向发展。

#### 📝 邮件列表

1. **[02-21 14:02]** [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[02-21 14:02]** [PATCH v8 1/6] arm64: Modify _midr_range() functions to read MIDR/REVIDR internally
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
3. **[02-21 14:02]** [PATCH v8 4/6] =?UTF-8?q?arm64:=20Make=20=C2=A0=5Fmidr=5Fin=5Fran?= =?UTF-8?q?ge=5Flist()=20an=20exported=20function?=
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
4. **[02-21 14:02]** [PATCH v8 5/6] smccc/kvm_guest: Enable errata based on implementation CPUs
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
5. **[02-26 19:39]** Re: [PATCH v8 1/6] arm64: Modify _midr_range() functions to read
 MIDR/REVIDR internally
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-26 19:40]** Re: [PATCH v8 4/6] arm64: =?iso-8859-1?Q?M?=
 =?iso-8859-1?B?YWtlIKBfbWlkcl9pbl9yYW5nZV9saXN0KCk=?= an exported function
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[02-26 19:41]** Re: [PATCH v8 5/6] smccc/kvm_guest: Enable errata based on
 implementation CPUs
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 17: [PATCH V2 0/5] mm: Rework generic PTDUMP configs

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 17 Feb 2025 09:52:15 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 Linux 内核的 PTDUMP 配置的重构，主要集中在 Anshuman Khandual 提出的五个补丁（PATCH V2 0/5）。这些补丁旨在清理和重命名与 PTDUMP 相关的配置，以提高可读性和清晰度。补丁包括删除特定平台的冗余配置、重命名配置项以消除混淆等。

在历史讨论中，Anshuman 提出了多个补丁的具体内容，例如在补丁 2/5 中提到可以从 mpc885_ads_defconfig 中删除 GENERIC_PTDUMP，因为它在 PowerPC 平台上被显式选择。此外，补丁 5/5 建议将 GENERIC_PTDUMP 和 PTDUMP_CORE 重命名为 ARCH_HAS_PTDUMP 和 PTDUMP，以更好地区分平台特性和功能启用。

在本周的新讨论中，Christophe Leroy 对补丁 2/5 和 5/5 提出了具体的建议和确认，表示同意删除不必要的条件判断，并更新提交信息以反映这些更改。Anshuman 也表示将根据讨论结果进行相应的修改。这些讨论显示出对补丁内容的积极反馈和进一步的完善。

#### 📝 邮件列表

1. **[02-17 09:52]** [PATCH V2 0/5] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-17 09:52]** [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-17 09:52]** [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-24 13:01]** Re: [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
5. **[02-24 13:04]** Re: [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from
 mpc885_ads_defconfig
   - 发件人: Christophe Leroy <christophe.leroy@csgroup.eu>
6. **[02-24 19:18]** Re: [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from
 mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-24 19:19]** Re: [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH 00/14] KVM: arm64: NV userspace ABI

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 15 Feb 2025 17:38:02 +0000

#### 🤖 AI 总结

本邮件线程讨论了 KVM（内核虚拟机）在 arm64 架构下的嵌套虚拟化（NV）用户空间 ABI 的一系列补丁。

1. **原始补丁内容**：Marc Zyngier 提出的补丁系列（共14个）旨在修正之前的 ABI 实现，确保其与 KVM 的当前操作方式一致。补丁中取消了对 NV 特定的后期调整，并通过 vcpu 标志完全选择 NV 配置，保留了 KVM_ARM_VCPU_EL2 标志以启用 VHE 下的 NV。

2. **之前讨论要点**：在历史讨论中，Marc 提出了多个补丁，涉及如何处理 NV_frac 作为 NV2 的同义词，以及在 VHE 禁用时强制 HCR.EL2.E2H 为 RES0 的必要性。这些讨论为本周的新进展奠定了基础。

3. **本周新讨论与进展**：本周的讨论主要围绕补丁的细节展开。Aneesh Kumar K.V 提出了对补丁中某些检查逻辑的质疑，认为在 MMFR1_EL1.VH 为零时检查 E2H0 的必要性值得商榷，并指出补丁中注册名称的错误。此外，Marc 对这些问题进行了回应，确认这些问题已在之前的版本中被提及，并表示希望保留当前代码实现，以避免潜在的更大问题。

总体来看，本周的讨论集中在补丁的细节和逻辑合理性上，参与者对补丁的有效性和实现方式进行了深入探讨。

#### 📝 邮件列表

1. **[02-15 17:38]** [PATCH 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-15 17:38]** [PATCH 01/14] arm64: cpufeature: Handle NV_frac as a synonym of NV2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-15 17:38]** [PATCH 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-24 13:09]** Re: [PATCH 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when
 ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
5. **[02-24 13:11]** Re: [PATCH 01/14] arm64: cpufeature: Handle NV_frac as a synonym of
 NV2
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
6. **[02-24 08:26]** Re: [PATCH 01/14] arm64: cpufeature: Handle NV_frac as a synonym of NV2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-24 08:32]** Re: [PATCH 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH 0/3] KVM: arm64: Separate the hyp FF-A buffers init from the host

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 26 Feb 2025 21:48:50 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是将 hypervisor FF-A（Firmware Framework for Arm）缓冲区的初始化与主机分开。该补丁系列包括三个主要部分：

1. **原始补丁内容**：补丁旨在将 hypervisor 的 FF-A 缓冲区初始化从主机的 FF-A 映射调用路径中分离出来，以避免在受保护模式下因无法映射缓冲区而拒绝任何 FF-A 调用。此外，还将错误映射的定义从 arm_ffa 驱动程序移动到 ffa 头文件中，以便 hyp 代码可以使用。

2. **之前讨论要点**：虽然本邮件没有详细记录历史讨论，但可以推测之前的讨论可能围绕如何优化 FF-A 的缓冲区管理以及确保在 hypervisor 和主机之间的安全通信。

3. **本周新讨论与进展**：本周的讨论中，Sebastian Ene 提出了三个补丁，分别涉及静态初始化版本锁、在 FF-A 初始化时映射 hypervisor 的缓冲区以及释放 hypervisor 接收缓冲区的所有权给 Trustzone。参与者 Sudeep Holla 建议将从驱动程序到头文件的代码移动分成单独的补丁，以避免与其他更改的冲突。Sebastian 同意了这一建议，并表示将会更新补丁。

总体而言，本周的讨论集中在补丁的具体实现和代码组织上，旨在提升 KVM 在 arm64 架构下的性能和安全性。

#### 📝 邮件列表

1. **[02-26 21:48]** [PATCH 0/3] KVM: arm64: Separate the hyp FF-A buffers init from the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
2. **[02-26 21:48]** [PATCH 1/3] KVM: arm64: Use the static initializer for the vesion lock
   - 发件人: Sebastian Ene <sebastianene@google.com>
3. **[02-26 21:48]** [PATCH 2/3] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
4. **[02-26 21:48]** [PATCH 3/3] KVM: arm64: Release the ownership of the hyp rx buffer to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
5. **[02-27 09:58]** Re: [PATCH 2/3] KVM: arm64: Map the hypervisor FF-A buffers on ffa
 init
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
6. **[02-27 17:58]** Re: [PATCH 2/3] KVM: arm64: Map the hypervisor FF-A buffers on ffa
 init
   - 发件人: Sebastian Ene <sebastianene@google.com>

---

### Thread 20: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 18 Feb 2025 17:34:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现可写 MIDR（模型 ID 寄存器）和 REVIDR（修订 ID 寄存器）的补丁系列。该补丁旨在允许虚拟机监控器（VMM）在不同机器之间迁移时修改这些寄存器，以便更好地处理错误管理。

在历史讨论中，Sebastian Ott 提出了该补丁系列的背景，指出这是在之前讨论的基础上进行的，且与 errata 管理系列相关联。补丁的更新包括处理 VPIDR_EL2 的上下文、让来宾能够观察到 MIDR_EL1 的变化、增加了额外的 .set_user 函数以及自测试功能。

在本周的新讨论中，Oliver Upton 对补丁提出了一些新问题，指出当前 KVM 允许来宾读取 SMIDR_EL1，尽管不支持 SME，并且 KVM 向用户空间呈现的“恒定”值来自启动 CPU，而非重置 ID 寄存器的 CPU。他表示将重新整理这些更改，以便解决这些问题，并希望在 6.15 版本中发布修复。Sebastian 对 Oliver 的反馈表示感谢，并确认他所做的工作看起来良好。整体来看，讨论集中在如何改进补丁以避免与现有实现的冲突。

#### 📝 邮件列表

1. **[02-18 17:34]** [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-24 14:23]** Re: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-26 17:47]** Re: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[02-26 10:56]** Re: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9

**📧 邮件数**: 4 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 24 Feb 2025 14:11:28 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH V2 7/7），目的是启用 EL2 对 FEAT_PMUv3p9 的要求。该补丁的核心内容是配置 MDCR_EL3.EnPM2 寄存器，以确保在支持 PMUv3p9 的情况下，相关的性能监控单元（PMU）功能能够正常工作。

在历史讨论中，参与者们关注了补丁的完整性，特别是是否遗漏了其他必要的寄存器配置。Mark Rutland 提到，MDCR_EL3.EnPM2 寄存器的配置在主线代码中未被描述，并且需要确认是否已测试过所有相关的要求。此外，他还指出该补丁可能需要添加稳定性和修复标签，以便于后续的维护。

在本周的新讨论中，Anshuman Khandual 提出了对补丁的具体修改建议，包括更新文档和添加修复标签。Rob Herring 和 Catalin Marinas 也参与了讨论，确认补丁尚未应用，并建议在确保所有要求都被满足后进行重新提交。总体来看，讨论集中在确保补丁的完整性和正确性上，以便在未来的内核版本中顺利实现 PMUv3p9 的支持。

#### 📝 邮件列表

1. **[02-24 14:11]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[02-25 11:47]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-26 11:14]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Rob Herring <robh@kernel.org>
4. **[02-26 17:44]** Re: [PATCH V2 7/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 22: [PATCH v2 00/14] KVM: arm64: NV userspace ABI

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 20 Feb 2025 13:48:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 NV（Nested Virtualization）用户空间 ABI（应用程序二进制接口）的更新。

**原始 patch/问题的内容**：
Marc Zyngier 提出的补丁系列（PATCH v2 00/14）旨在修正之前版本的 ABI，确保其与 KVM 当前的操作方式一致。补丁中移除了 NV 特定的调整，并通过 vcpu 标志完全选择 NV 配置，保留了 KVM_ARM_VCPU_EL2 标志以启用 VHE（Virtualization Host Extensions），并新增了 KVM_ARM_VCPU_EL2_E2H0 标志以限制 NV 行为。

**之前讨论要点**：
在之前的讨论中，Marc 提到 NV 的支持将有两种互斥配置：VHE-only 和 mVHE-only，后者不支持递归虚拟化。为此，引入了新的 vcpu 特性标志以表示第二种配置。

**本周的新讨论、进展或结论**：
本周的讨论中，Aneesh Kumar K.V 对补丁中的术语进行了修改，建议将 "mVHE-only" 改为 "nVHE-only"。Oliver Upton 则确认修复了补丁中的拼写错误，并表示已将补丁应用到下一个版本中，感谢 Marc 的贡献。补丁的多个部分已被逐步应用，显示出该系列补丁的进展顺利。

#### 📝 邮件列表

1. **[02-20 13:48]** [PATCH v2 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-20 13:49]** [PATCH v2 10/14] KVM: arm64: Allow userspace to limit NV support to nVHE
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-24 15:14]** Re: [PATCH v2 10/14] KVM: arm64: Allow userspace to limit NV
 support to nVHE
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
4. **[02-24 11:52]** Re: (subset) [PATCH v2 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 23: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 10:12:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下内存管理的补丁系列，主要内容是移除 PXD_TABLE_BIT。Anshuman Khandual 提出的补丁（PATCH V2 0/8）旨在通过依赖 PXX_TYPE_MASK、PXX_TYPE_SECT 和 PXX_TYPE_TABLE 来替代 PXX_TABLE_BIT，这样的抽象方式对于即将支持的 D128 页表非常重要，因为 D128 页表没有单一的页表位来区分表和块，而是使用跳过级别（SKL）字段。

在之前的讨论中，参与者们关注了补丁的逻辑正确性，并一致同意移除 PXX_TABLE_BIT 的意图。Anshuman Khandual 在邮件中询问了补丁系列的更新进展。

在本周的新讨论中，Ryan Roberts 对补丁提出了建议，他认为将所有移除 PXX_TABLE_BIT 的修改合并为一个单独的补丁会更易于审查，并且可以提供更清晰的提交日志。他还提到，当前的七个提交日志并不十分有帮助。Ryan 认为这样的调整将有助于更好地理解变更的理由。

#### 📝 邮件列表

1. **[02-21 10:12]** [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-28 09:12]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-28 15:32]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>

---

### Thread 24: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 1 Mar 2025 07:58:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一组补丁（PATCH V2 0/7），旨在为 FEAT_PMUv3p9 启用 EL2 的要求，主要针对 arm64 架构的引导过程。

在历史讨论中，虽然没有具体的邮件记录，但可以推测这些补丁是为了确保在引导过程中满足特定的硬件性能监控单元（PMU）要求。补丁的前六个部分已经被应用，并且在与相关文档（.xml）对比后，参与者 Will Deacon 确认它们是正确的，并给予了认可（Acked-by）。他还提到最后一个补丁将被 Catalin Marinas 删除或替换。

在本周的新讨论中，Will Deacon 再次确认了前六个补丁的正确性，并提到 Catalin 将会处理最后一个补丁。Catalin Marinas 随后回应表示他已经删除了最后一个补丁，并计划将新的补丁排入队列。这表明讨论进展顺利，补丁的整合工作正在进行中。

#### 📝 邮件列表

1. **[03-01 07:58]** Re: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Will Deacon <will@kernel.org>
2. **[03-01 11:11]** Re: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 25: [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 02 Mar 2025 17:12:54 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 中 ARM64 平台的性能监控单元（PMU）相关寄存器设置的问题。原始的补丁（patch）旨在修复 `SET_ONE_REG` 操作对虚拟性能监控计数器（vPMC）寄存器的影响，确保在设置这些寄存器时能够重置当前的性能事件计数。

在历史讨论中，提到之前的提交（commit 9228b26194d1）已修复了 `GET_ONE_REG` 操作，但在 `SET_ONE_REG` 的实现中仍存在问题。具体来说，当用户空间通过 `KVM_SET_ONE_REG` 写入 vPMC 寄存器时，KVM 只更新了系统寄存器文件中的值，而没有重置当前的性能事件计数，这导致了寄存器值的不一致。

在本周的新讨论中，Akihiko Odaki 提出了具体的补丁代码，增加了对 `set_pmu_evcntr` 函数的实现，以调用 `kvm_pmu_set_counter_value()` 来同时更新当前的性能事件计数。该补丁通过修改 `sys_regs.c` 文件，确保在设置 vPMC 寄存器时能够正确处理计数器的值。补丁已提交并标记为修复之前的错误。

总结来说，本周的讨论集中在修复 KVM ARM64 平台中 vPMC 寄存器的设置逻辑，以确保性能计数的准确性。

#### 📝 邮件列表

1. **[03-02 17:12]** [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>

---

### Thread 26: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 28 Feb 2025 12:13:55 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在统计 pKVM（paravirtualized KVM）在二级页表中的使用情况。补丁的主要内容是将 pKVM 在内存统计中的页数计算纳入二级页表统计，与 VHE（Virtualization Host Extensions）模式的处理方式相似。

在历史讨论中没有提供具体的背景信息，但本周的讨论由 Vincent Donnefort 提出，补丁的代码修改涉及到内存管理的函数，增加了对 pKVM 页表页面的统计功能。这一改动将有助于更准确地监控和管理虚拟化环境中的内存使用情况。

本周的进展主要集中在补丁的具体实现上，Vincent Donnefort 提交了补丁，并详细说明了代码的修改部分，强调了对内存统计的影响。补丁的签名也表明了其作者的身份。整体来看，这一补丁的提出是为了提升 KVM 在 arm64 架构下的性能监控能力。

#### 📝 邮件列表

1. **[02-28 12:13]** [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 27: [PATCH v4] arm64: Add basic MTE test

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 27 Feb 2025 15:22:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的基本 MTE（内存标签扩展）测试的补丁（PATCH v4）。该补丁主要用于测试标签存储访问和不同 MTE 模式下的标签不匹配情况。

在历史讨论中，未提供相关背景信息，邮件列表中没有之前的讨论记录。

本周的讨论中，Vladimir Murzin 提交了该补丁，详细描述了补丁的实现内容，包括对多个文件的修改和新增 MTE 测试的代码。补丁中新增了 `arm/mte.c` 文件，包含了 MTE 测试的核心逻辑，以及对 MTE 模式的支持。补丁还修改了 Makefile 和其他相关文件，以便于编译和运行新的测试用例。

本周的进展主要集中在补丁的具体实现上，补丁通过引入新的测试用例，旨在验证 MTE 功能的正确性。参与者对补丁的内容表示支持，并期待进一步的测试结果。整体来看，该补丁为 ARM64 架构下的 MTE 功能提供了基础的测试框架，推动了相关技术的进展。

#### 📝 邮件列表

1. **[02-27 15:22]** [PATCH v4] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>

---

### Thread 28: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 27 Feb 2025 09:21:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的 EL2 需求，以支持 FEAT_PMUv3p9 特性。原始的补丁（PATCH V3）旨在通过添加一个新的初始化助手函数 `__init_el2_fgt2()`，来配置细粒度陷阱控制寄存器 HDFGRTR2_EL2 和 HDFGWTR2_EL2，以便允许从 EL1 访问 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1 寄存器。

在之前的讨论中，补丁的背景主要集中在如何确保在进入内核时，相关寄存器的访问权限得到正确配置，以避免陷入 EL2 的问题。补丁还更新了文档，明确了在使用 FEAT_FGT2 特性时，SCR_EL3.FGTEn2 的初始化要求。

本周的新讨论中，补丁的作者 Anshuman Khandual 提到了本次补丁的更新，包括根据评审者 Mark 的建议，添加了 MDCR_EL3.EnPM2 的引导要求，并增加了 'Fixes:' 和 'CC: stable' 标签。此外，补丁经过了 Rob Herring 的测试和审查，确保其功能的可靠性。整体来看，本周的讨论主要是对补丁内容的完善和确认。

#### 📝 邮件列表

1. **[02-27 09:21]** [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 17:45:26 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于在 kvm-unit-tests 库中将 `__ASSEMBLY__` 替换为 `__ASSEMBLER__` 的补丁（patch）。历史讨论中，Sean Christopherson 提出了这个补丁，目的是将所有非 x86 的条件编译指令从 `__ASSEMBLY__` 转换为 `__ASSEMBLER__`，并移除手动定义的 `__ASSEMBLY__`。他指出，`__ASSEMBLY__` 是从 Linux 内核继承而来，需要手动定义，而 `__ASSEMBLER__` 是编译器在预处理汇编时自动定义的，因此更为可靠。

在本周的新讨论中，Andrew Jones 对该补丁进行了审查，并指出除了 x86 外，只有一个地方错误地拼写了 `__ASSEMBLY__`，并在注释中出现。Andrew 表示他已对 RISC-V 和 ARM 的相关部分进行了审核，并给予了“审核通过”（Reviewed-by）的反馈。

总结而言，此次讨论主要集中在改进代码的可维护性和可靠性上，通过替换宏定义来简化编译过程。

#### 📝 邮件列表

1. **[02-21 17:45]** [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[02-25 14:37]** Re: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of
 __ASSEMBLY__
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.14, take #3

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 17:44:06 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，目的是解决 Linux 6.14 版本中的一些 MMU（内存管理单元）相关的错误。

在历史讨论中，Marc Zyngier 提到此次补丁主要集中在两个 MMU 错误上：一个是影响 hVHE EL2 的 stage-1，错误地从错误的寄存器中获取 ASID（地址空间标识符）；另一个是影响 VHE（虚拟化扩展），允许其使用过时的 VMID（虚拟机标识符）。Marc 强调这些问题的严重性，并请求将这些修复纳入主线。

在本周的新讨论中，Paolo Bonzini 回复确认已将补丁合并，并对 Marc 表示感谢。这表明修复工作得到了认可并顺利推进。

总结而言，此次讨论围绕 KVM/arm64 的 MMU 修复补丁展开，历史讨论中指出了具体的错误和其影响，而本周的进展则是补丁已被成功合并。

#### 📝 邮件列表

1. **[02-20 17:44]** [GIT PULL] KVM/arm64 fixes for 6.14, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-24 19:20]** Re: [GIT PULL] KVM/arm64 fixes for 6.14, take #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 13:57:38 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 arm64 架构的基本 MTE（Memory Tagging Extension）测试的补丁（PATCH v3）。该补丁旨在增强 KVM 单元测试的功能，特别是在内存标记扩展方面。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁经过了多轮审查，参与者对其重要性和实用性表示认可。Alexandru Elisei 提到，测试中未能找到页表项（PTE）可能由多种问题引起，包括内存分配器的错误等，但他认为这个测试非常有用，并不认为这是一个阻碍因素。

在本周的新讨论中，Alexandru 对补丁的审查表示赞同，并指出可能会有其他问题需要解决。Andrew Jones 表示如果补丁准备好，他乐意合并，并询问是否会有 v4 版本。Vladimir Murzin 确认会根据 Alex 的反馈进行调整。

综上所述，该补丁的讨论进展顺利，参与者积极反馈，后续将进行必要的修改以便最终合并。

#### 📝 邮件列表

1. **[02-27 13:57]** Re: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[02-27 15:29]** Re: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[02-27 14:33]** Re: [kvm-unit-tests PATCH v3] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v1 0/7] arm64: support EL2

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 14:13:47 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是为 ARM64 架构的 KVM 单元测试添加对 EL2 的支持，包含七个补丁。历史讨论中，Joey Gouly 提出了这一系列补丁的目的，主要是为了在 EL2 级别运行 KVM 单元测试，并为后续的嵌套虚拟化测试做准备。补丁中包括了在 EL2 启动时降级到 EL1 的处理、使用虚拟化计时器、修复计时器中断、更新自测试以及在 EL2 计数周期等功能。

在之前的讨论中，Joey 提到了一些未测试的 EFI/ACPI 变更和 PMU 测试的问题，并且对调试测试的失败进行了说明。Alexandru Elisei 对补丁的多个部分进行了审查，提出了一些细节上的建议和确认，认为大部分补丁都符合要求，并给予了“Reviewed-by”的标记。

本周的新讨论中，Alex 对补丁的具体实现提出了一些问题和建议，特别是关于 EL2 寄存器初始化的可靠性、计时器中断的处理以及 PMU 计数逻辑的合理性。总体来看，本周的讨论集中在对补丁细节的审查和进一步的技术探讨上，推动了补丁的完善和确认。

#### 📝 邮件列表

1. **[02-20 14:13]** [kvm-unit-tests PATCH v1 0/7] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[02-20 14:13]** [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[02-20 14:13]** [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[02-20 14:13]** [kvm-unit-tests PATCH v1 3/7] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[02-20 14:13]** [kvm-unit-tests PATCH v1 5/7] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[02-20 14:13]** [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[02-27 16:53]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[02-27 16:55]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[02-27 16:58]** Re: [kvm-unit-tests PATCH v1 3/7] arm64: micro-bench: fix timer IRQ
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[02-27 16:58]** Re: [kvm-unit-tests PATCH v1 5/7] arm64: selftest: update test for
 running at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[02-27 17:01]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: writable ID_AA64MMFR0_EL1.TGRAN*_2 ?

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 28 Feb 2025 16:19:06 +0100 (CET)

#### 🤖 AI 总结

本邮件讨论的主题是关于可写的 ID_AA64MMFR0_EL1.TGRAN*_2 寄存器。Sebastian Ott 提出了一个问题，涉及在两个 Graviton 主机之间迁移时，TGRAN*_2 寄存器的可写性问题。他指出，这两个主机支持相同的 S2 大小，但表达方式不同（2 表示支持，而 0 表示“查看 TGRAN*”）。

在本周的讨论中，Sebastian 提出了两个可能的解决方案：一是将这些寄存器的访客视图设置为 NI（不适用）以适应“正常”或非嵌套的访客；二是允许在这两个值之间转换，并可能允许写入 NI 以确保兼容性。

目前尚未有其他参与者的回复或进一步的讨论，因此该问题仍在等待社区的反馈和建议。

#### 📝 邮件列表

1. **[02-28 16:19]** writable ID_AA64MMFR0_EL1.TGRAN*_2 ?
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

