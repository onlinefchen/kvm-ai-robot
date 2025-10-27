# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 12:11:49

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 127
- **总 Thread 数**: 16
- **大型 Thread** (>20封): 1 个

### 分类分布

- **PATCH**: 13 threads (118 邮件)
- **RFC**: 1 threads (6 邮件)
- **Bug Report**: 1 threads (1 邮件)
- **GIT PULL**: 1 threads (2 邮件)

---

## 📌 PATCH

共 13 个 thread

---

### Thread 1: [PATCH v5 00/12] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 22 | **👥 参与者**: 5 | **📅 开始时间**: Thu, 28 Aug 2025 09:39:14 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v5 00/12] Direct Map Removal Support for guest_memfd”的补丁系列，主要目的是为 KVM 的 guest_memfd 提供直接映射移除的支持，以防止 Spectre 风格的攻击。

**原始补丁/问题内容**：
该补丁系列扩展了 guest_memfd 的功能，使其能够从主机内核的直接映射中移除虚拟机的内存。通过这种方式，如果内核页表不包含指向来宾内存的条目，则任何通过直接映射的推测性读取都将被 MMU 阻止，从而增强安全性。

**之前讨论要点**：
在历史讨论中，参与者讨论了如何通过将 guest_memfd 的内存移除直接映射来提高安全性，并且补丁的设计基于 guest_memfd 对“非机密虚拟机”的支持。补丁还涉及到如何处理 KVM 内部访问来宾内存的方式，以确保性能和功能的平衡。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现和测试上。补丁引入了新的标志 GUEST_MEMFD_FLAG_NO_DIRECT_MAP，允许用户在创建 guest_memfd 时选择是否移除直接映射。此外，补丁还对 KVM 的自测试进行了扩展，以确保在直接映射被移除的情况下，来宾内存的读写操作能够正常进行。参与者还讨论了补丁的文档和代码的清晰性，提出了一些改进建议，并对补丁的整体方向表示支持。

#### 📝 邮件列表

1. **[08-28 09:39]** [PATCH v5 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
2. **[08-28 09:39]** [PATCH v5 01/12] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
3. **[08-28 09:39]** [PATCH v5 02/12] arch: export set_direct_map_valid_noflush to KVM
 module
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
4. **[08-28 09:39]** [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
5. **[08-28 09:39]** [PATCH v5 04/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
6. **[08-28 09:39]** [PATCH v5 05/12] KVM: Documentation: describe
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
7. **[08-28 09:39]** [PATCH v5 06/12] KVM: selftests: load elf via bounce buffer
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
8. **[08-28 09:39]** [PATCH v5 07/12] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
9. **[08-28 09:39]** [PATCH v5 08/12] KVM: selftests: Add guest_memfd based
 vm_mem_backing_src_types
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
10. **[08-28 09:39]** [PATCH v5 09/12] KVM: selftests: stuff vm_mem_backing_src_type into
 vm_shape
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
11. **[08-28 09:39]** [PATCH v5 10/12] KVM: selftests: cover GUEST_MEMFD_FLAG_NO_DIRECT_MAP
 in mem conversion tests
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
12. **[08-28 09:39]** [PATCH v5 11/12] KVM: selftests: cover GUEST_MEMFD_FLAG_NO_DIRECT_MAP
 in guest_memfd_test.c
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
13. **[08-28 09:39]** [PATCH v5 12/12] KVM: selftests: Test guest execution from direct map
 removed gmem
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
14. **[08-28 11:07]** Re: [PATCH v5 02/12] arch: export set_direct_map_valid_noflush to KVM module
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[08-28 11:21]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[08-28 12:26]** Re: [PATCH v5 11/12] KVM: selftests: cover
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP in guest_memfd_test.c
   - 发件人: David Hildenbrand <david@redhat.com>
17. **[08-28 12:27]** Re: [PATCH v5 05/12] KVM: Documentation: describe
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
18. **[08-28 14:50]** Re: [PATCH v5 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: David Hildenbrand <david@redhat.com>
19. **[08-28 17:26]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Mike Rapoport <rppt@kernel.org>
20. **[08-28 17:54]** Re: [PATCH v5 04/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
21. **[08-28 23:00]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
22. **[08-31 18:26]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 2: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs

**📧 邮件数**: 19 | **👥 参与者**: 6 | **📅 开始时间**: Mon, 25 Aug 2025 13:06:17 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 Hyper-V 驱动中的 `NEED_RESCHED_LAZY` 问题，并使用通用 API 的一系列补丁。

1. **原始补丁内容**：该补丁系列（共5个补丁）旨在修复 MSHV 根分区未能正确处理 `NEED_RESCHED_LAZY` 的问题，并通过将与 TIF 相关的 MSHV 代码去重，转变为更通用的 "virt" API。

2. **之前讨论要点**：在历史讨论中，参与者关注如何简化和通用化 Hyper-V 驱动中的代码，以提高可维护性和可重用性。补丁的设计初衷是消除与 KVM 相关的特定依赖，使得代码可以被其他虚拟化平台使用。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现和后续步骤上。Sean Christopherson 提到可能将补丁通过 tip tree 提交。Wei Liu 和 Nuno Das Neves 对补丁的测试和整合提出了建议，强调需要在 mshv_vtl_main.c 中进行类似的更改。Nuno 还建议将所有 mshv 驱动的更改合并为一个补丁，以简化维护。讨论中还提到了一些潜在的依赖问题，参与者们一致认为需要在提交过程中考虑到这些问题，以确保代码的清晰性和可追溯性。

#### 📝 邮件列表

1. **[08-25 13:06]** [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-25 13:06]** [PATCH 1/5] Drivers: hv: Move TIF pre-guest work handling fully into mshv_common.c
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-25 13:06]** [PATCH 2/5] Drivers: hv: Handle NEED_RESCHED_LAZY before transferring
 to guest
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[08-25 13:06]** [PATCH 3/5] entry/kvm: KVM: Move KVM details related to signal/-EINTR
 into KVM proper
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-25 13:06]** [PATCH 4/5] entry: Rename "kvm" entry code assets to "virt" to
 genericize APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[08-25 13:06]** [PATCH 5/5] Drivers: hv: Use common "entry virt" APIs to do work
 before running guest
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-25 21:45]** Re: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Wei Liu <wei.liu@kernel.org>
8. **[08-26 00:23]** Re: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
9. **[08-25 22:26]** Re: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Wei Liu <wei.liu@kernel.org>
10. **[08-25 16:08]** Re: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Nuno Das Neves <nunodasneves@linux.microsoft.com>
11. **[08-25 17:27]** Re: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[08-26 16:58]** Re: [PATCH 0/5] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Wei Liu <wei.liu@kernel.org>
13. **[08-28 10:59]** [PATCH 0/5] KVM: arm64: GICv5 legacy (GCIE_LEGACY) NV enablement and
 cleanup
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[08-28 10:59]** [PATCH 2/5] KVM: arm64: Enable nested for GICv5 host with
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[08-28 10:59]** [PATCH 4/5] KVM: arm64: Use ARM64_HAS_GICV5_LEGACY for GICv5 probing
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[08-28 10:59]** [PATCH 3/5] arm64: cpucaps: Add GICv5 Legacy vCPU interface
 (GCIE_LEGACY) capability
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[08-28 10:59]** [PATCH 1/5] KVM: arm64: Allow ICC_SRE_EL2 accesses on a GICv5 host
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[08-28 10:59]** [PATCH 5/5] irqchip/gic-v5: Drop has_gcie_v3_compat from gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[08-28 15:05]** Re: [PATCH 1/5] KVM: arm64: Allow ICC_SRE_EL2 accesses on a GICv5 host
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW

**📧 邮件数**: 17 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 27 Aug 2025 17:10:22 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要聚焦于 S1 页表走查（PTW）中的 TTW（Translation Table Walk）报告和 52 位物理地址（PA）的支持。

**原始 patch/问题内容**：
该补丁系列的目标是解决在 S1PTW 故障注入时，未能报告走查级别的问题。这种情况违反了架构规范，且该问题源于早期没有实现 S1 页表走查的历史。

**之前讨论要点**：
在历史讨论中，Marc Zyngier 提到当前代码强制使用 48 位地址，而 NV（Nested Virtualization）实现尚未支持 52 位 PA。补丁旨在扩展 S1 PTW，以支持 LPA（Large Physical Address）和 LPA2，同时引入一个过滤机制，以便在访问故障地址时报告走查的起始级别。

**本周的新讨论、进展或结论**：
本周的讨论中，Marc Zyngier 提交了 16 个补丁，涵盖了多个方面，包括：
1. 计算 52 位 PA 支持状态的辅助函数。
2. 计算最大输出地址时考虑 52 位 PA。
3. 处理 52 位 TTBR 地址和对齐检查。
4. 允许非 NV 虚拟 CPU 使用 S1 PTW。
5. 在故障注入路径中集成新的走查机制，以便在 ESR_ELx 寄存器中填充翻译级别。

此外，还扩展了自测用例，以确保在 S1PTW 故障时能够正确报告级别。这些补丁的实施将增强 KVM 在 arm64 架构下的功能和合规性，确保更准确的故障报告和地址处理。

#### 📝 邮件列表

1. **[08-27 17:10]** [PATCH 00/16] KVM: arm64: TTW reporting on SEA and 52bit PA in S1 PTW
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-27 17:10]** [PATCH 01/16] KVM: arm64: Add helper computing the state of 52bit PA support
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[08-27 17:10]** [PATCH 02/16] KVM: arm64: Account for 52bit when computing maximum OA
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-27 17:10]** [PATCH 03/16] KVM: arm64: Compute 52bit TTBR address and alignment
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[08-27 17:10]** [PATCH 04/16] KVM: arm64: Decouple output address from the PT descriptor
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[08-27 17:10]** [PATCH 05/16] KVM: arm64: Pass the walk_info structure to compute_par_s1()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[08-27 17:10]** [PATCH 06/16] KVM: arm64: Compute shareability for LPA2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[08-27 17:10]** [PATCH 07/16] KVM: arm64: Populate PAR_EL1 with 52bit addresses
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[08-27 17:10]** [PATCH 08/16] KVM: arm64: Expand valid block mappings to FEAT_LPA/LPA2 support
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[08-27 17:10]** [PATCH 09/16] KVM: arm64: Report faults from S1 walk setup at the expected start level
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[08-27 17:10]** [PATCH 10/16] KVM: arm64: Allow use of S1 PTW for non-NV vcpus
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[08-27 17:10]** [PATCH 11/16] KVM: arm64: Allow EL1 control registers to be accessed from the CPU state
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[08-27 17:10]** [PATCH 12/16] KVM: arm64: Don't switch MMU on translation from non-NV context
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[08-27 17:10]** [PATCH 13/16] KVM: arm64: Add filtering hook to S1 page table walk
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[08-27 17:10]** [PATCH 14/16] KVM: arm64: Add S1 IPA to page table level walker
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[08-27 17:10]** [PATCH 15/16] KVM: arm64: Populate level on S1PTW SEA injection
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[08-27 17:10]** [PATCH 16/16] KVM: arm64: selftest: Expand external_aborts test to look for TTW levels
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 27 Aug 2025 17:01:49 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 Hyper-V 驱动中的 `NEED_RESCHED_LAZY` 问题，并使用通用 API 的补丁系列（PATCH v2 0/7）。该补丁旨在解决 MSHV 根分区及上层 VTL 代码未能正确处理 `NEED_RESCHED_LAZY` 的错误，并通过将与 TIF 相关的 MSHV 代码去重，将“kvm”入口 API 转换为更通用的“virt” API。

在历史讨论中，补丁的背景主要集中在如何确保在转移控制到客人之前，能够正确检查和处理 `NEED_RESCHED_LAZY`，以避免不必要的延迟。Sean Christopherson 提到，补丁系列依赖于即将合并的 VTL 更改，并表示只有 Hyper-V 团队会受到影响。

本周的新讨论中，Sean 提交了补丁的多个版本，逐一修复了与 VTL 返回取消、IRQ 处理顺序等相关的问题。Nuno Das Neves 对第一个补丁进行了测试并给予了认可，表示其在启用 `CONFIG_PREEMPT_LAZY` 后能够正常工作。Wei Liu 则提到将从其树中删除相关驱动，因为对其引入的 ABI 存在异议，并未打算应用某些补丁。

总体来看，本周讨论集中在补丁的测试和修复进展上，部分补丁得到了认可，但也面临着 ABI 方面的挑战。

#### 📝 邮件列表

1. **[08-27 17:01]** [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-27 17:01]** [PATCH v2 1/7] Drivers: hv: Handle NEED_RESCHED_LAZY before
 transferring to guest
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-27 17:01]** [PATCH v2 2/7] Drivers: hv: Disentangle VTL return cancellation from SIGPENDING
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[08-27 17:01]** [PATCH v2 3/7] Drivers: hv: Disable IRQs only after handling pending
 work before VTL return
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-27 17:01]** [PATCH v2 4/7] entry/kvm: KVM: Move KVM details related to
 signal/-EINTR into KVM proper
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[08-27 17:01]** [PATCH v2 5/7] entry: Rename "kvm" entry code assets to "virt" to
 genericize APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-27 17:01]** [PATCH v2 6/7] Drivers: hv: Use common "entry virt" APIs to do work
 in root before running guest
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[08-27 17:01]** [PATCH v2 7/7] Drivers: hv: Use "entry virt" APIs to do work before
 returning to lower VTL
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[08-28 16:56]** Re: [PATCH v2 1/7] Drivers: hv: Handle NEED_RESCHED_LAZY before
 transferring to guest
   - 发件人: Nuno Das Neves <nunodasneves@linux.microsoft.com>
10. **[08-28 17:03]** Re: [PATCH v2 6/7] Drivers: hv: Use common "entry virt" APIs to do
 work in root before running guest
   - 发件人: Nuno Das Neves <nunodasneves@linux.microsoft.com>
11. **[08-29 18:38]** Re: [PATCH v2 2/7] Drivers: hv: Disentangle VTL return cancellation
 from SIGPENDING
   - 发件人: Wei Liu <wei.liu@kernel.org>

---

### Thread 5: [PATCH v3 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 27 Aug 2025 11:19:40 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 pKVM（Protected KVM）虚拟机处理的改进，主要集中在如何在虚拟机初始化过程中更早地保留 pKVM 句柄。

**原始 patch/问题的内容**：
该补丁系列的目标是确保在虚拟机初始化时能够及时分配 pKVM 句柄，以避免在主机 MMU 通知时出现句柄未分配的情况。当前，句柄的分配仅在第一次 vCPU 运行时进行，这可能导致在虚拟机的内存与主机 MMU 关联后，出现无效的 MMU 通知。

**之前讨论要点**：
历史讨论中提到，pKVM 句柄的分配时机不当可能导致系统不稳定，因此需要重构代码以便在虚拟机初始化时就保留句柄。补丁系列还包括对现有代码的重命名和文档修正，以提高代码的可读性和维护性。

**本周的新讨论、进展或结论**：
本周的讨论主要围绕补丁的具体实现，包括：
1. 引入新的超调用接口，将虚拟机的保留和初始化过程分为两个阶段，以便主机可以更灵活地管理虚拟机的生命周期。
2. 在 `pkvm_init_host_vm` 函数中，提前保留 pKVM 句柄，确保在虚拟机的内存准备好之前就能获得有效的句柄。
3. 代码重构以简化虚拟机表项的插入和状态管理，使得后续的开发和维护更加高效。

整体来看，本周的讨论和补丁推进了 pKVM 的稳定性和可维护性，为未来的功能扩展打下了良好的基础。

#### 📝 邮件列表

1. **[08-27 11:19]** [PATCH v3 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-27 11:19]** [PATCH v3 1/9] KVM: arm64: Add build-time check for duplicate
 DECLARE_REG use
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-27 11:19]** [PATCH v3 2/9] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[08-27 11:19]** [PATCH v3 3/9] KVM: arm64: Rename 'host_kvm' to 'kvm' in pKVM host code
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-27 11:19]** [PATCH v3 4/9] KVM: arm64: Clarify comments to distinguish pKVM mode
 from protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[08-27 11:19]** [PATCH v3 5/9] KVM: arm64: Decouple hyp VM creation state from its handle
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[08-27 11:19]** [PATCH v3 6/9] KVM: arm64: Separate allocation and insertion of pKVM
 VM table entries
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[08-27 11:19]** [PATCH v3 7/9] KVM: arm64: Consolidate pKVM hypervisor VM
 initialization logic
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[08-27 11:19]** [PATCH v3 8/9] KVM: arm64: Introduce separate hypercalls for pKVM VM
 reservation and initialization
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[08-27 11:19]** [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 6: [PATCH] KVM: selftests: fix irqfd_test on arm64

**📧 邮件数**: 8 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 25 Aug 2025 17:52:03 +0200

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM 的自测试（selftests）中，修复 arm64 平台上的 irqfd_test 测试。原始的补丁由 Sebastian Ott 提交，目的是解决在运行 irqfd_test 时出现的资源不可用错误。补丁通过为虚拟机（VM）设置虚拟通用中断控制器（vgic）来修复该问题。

在之前的讨论中，参与者们探讨了如何在 KVM 的虚拟机创建过程中更智能地处理 vgic 的创建。Sean Christopherson 提出，虽然不一定需要使用 v3 版本的 vgic，但应当根据可用的硬件来选择合适的 vgic。Marc Zyngier 强调，创建 vgic 的选择必须明确，不能依赖于模糊的假设。

本周的新讨论中，Oliver Upton 提出了一个建议，即为需要特定 vgic 配置的测试提供一个专用的创建 VM 的 API，而不是在通用的 vm_create() 中隐式处理 vgic。Sean Christopherson 进一步强调，过多的默认配置可能会使测试意图不明确，因此应当保持测试的清晰性。讨论中还提到，可能需要提供一个 API 来初始化一个简化的 GIC，以便于测试的灵活性。

总体来看，邮件讨论围绕如何在 KVM 的自测试中更有效地管理 vgic 的创建与配置展开，旨在提高测试的可读性和灵活性。

#### 📝 邮件列表

1. **[08-25 17:52]** [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[08-25 12:52]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-25 21:51]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-25 14:11]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-25 14:38]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[08-26 11:51]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-26 12:24]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[08-26 13:41]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 7: [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and
 generation script

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 29 Aug 2025 10:51:40 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的系统寄存器（sysreg）字段定义及生成脚本的修复和改进。Fuad Tabba 提出了一个包含三个补丁的系列（PATCH v3 0/3），主要内容如下：

1. **原始补丁内容**：补丁旨在修复 sysreg 定义文件中的错误，包括将 NSACR_RFR 的值从 0b0001 更正为 0b0010，并修正 EIESB 和 DoubleLock 的符号定义。此外，补丁还删除了一些冗余的定义，以减少未来可能出现的错误。

2. **之前讨论要点**：在之前的讨论中，参与者对补丁的必要性和结构进行了评估，认为将 NSACR_RFR 的修复与其他清理工作分开可能更为理想。整体上，补丁得到了积极的反馈，并获得了多个参与者的认可。

3. **本周新讨论与进展**：本周的讨论集中在补丁的具体实现上。Fuad 提出了对生成脚本的验证检查，以捕获潜在的重复定义和错误，确保生成的头文件正确无误。Mark Rutland 对每个补丁表示支持，并提出了一些改进建议，例如将 SysregFields 和 Sysregs 视为一个组，以便更好地捕获定义重复的情况。整体来看，本周讨论积极，补丁得到了认可，且有助于提高代码的质量和可靠性。

#### 📝 邮件列表

1. **[08-29 10:51]** [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and
 generation script
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-29 10:51]** [PATCH v3 1/3] arm64: sysreg: Fix and tidy up sysreg field definitions
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-29 10:51]** [PATCH v3 2/3] arm64: sysreg: Correct sign definitions for EIESB and DoubleLock
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[08-29 10:51]** [PATCH v3 3/3] arm64: sysreg: Add validation checks to sysreg header
 generation script
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-29 11:07]** Re: [PATCH v3 1/3] arm64: sysreg: Fix and tidy up sysreg field
 definitions
   - 发件人: Mark Rutland <mark.rutland@arm.com>
6. **[08-29 11:10]** Re: [PATCH v3 2/3] arm64: sysreg: Correct sign definitions for EIESB
 and DoubleLock
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[08-29 11:14]** Re: [PATCH v3 3/3] arm64: sysreg: Add validation checks to sysreg
 header generation script
   - 发件人: Mark Rutland <mark.rutland@arm.com>

---

### Thread 8: [PATCH V2 0/2] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 29 Aug 2025 11:32:13 +0530

#### 🤖 AI 总结

本邮件讨论的主题是对 ARM64 架构中 TCR_EL1 寄存器字段宏的清理和更新。Anshuman Khandual 提出了两个补丁（PATCH V2 0/2），旨在通过更新寄存器字段定义和替换宏来简化代码。

**原始补丁内容**：
补丁的主要目的是清理分散在 ARM64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏。具体来说，TCR_XXX 宏被移动到 KVM 头文件（asm/kvm_arm.h），以便在 KVM 中继续使用，同时不引入功能性变化。

**之前讨论要点**：
在补丁的 V1 版本中，提出了对 ARM ARM 版本的修正、宏定义的更改等。补丁 V2 版本中，Anshuman 进一步修正了 ARM ARM 版本，调整了枚举类型，并删除了 KVM 代码中的所有 TCR_EL1 替换。

**本周新讨论与进展**：
本周的讨论中，Marc Zyngier 对补丁提出了质疑，认为不应在没有必要的情况下重复定义宏，并建议使用脚本来表达新旧定义之间的关系。Anshuman 随后表示将审计这些移动的宏，并考虑删除当前未在 KVM 中使用的宏。同时，他尝试将这些宏表达为之前定义的 TCR_EL1 字段定义的形式，以确保代码的整洁性和一致性。

#### 📝 邮件列表

1. **[08-29 11:32]** [PATCH V2 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[08-29 11:32]** [PATCH V2 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[08-29 11:32]** [PATCH V2 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[08-29 09:13]** Re: [PATCH V2 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[08-29 19:04]** Re: [PATCH V2 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 9: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 27 Aug 2025 10:43:54 +0200

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）中启用 mmap() 函数以支持 guest_memfd 的补丁（PATCH v17 00/24）。该补丁旨在改善虚拟机内存管理，允许通过内存映射文件描述符来访问虚拟机的内存。

在之前的讨论中，补丁的内容和目的已经明确，参与者们对其功能表示认可，并进行了相关的技术评估。

本周的新讨论中，Paolo Bonzini 确认已将该补丁应用到 kvm/next 分支，并感谢 Sean Christopherson 的工作。Sean 也表示他对 arm64 相关的更改进行了独立测试，结果与之前一致，确认无误。此外，Marc Zyngier 提出希望为这些补丁创建一个稳定分支，以便于处理未来可能出现的冲突。Paolo 对此表示同意，并提供了将补丁推送到特定分支的建议。最终，Marc 确认已成功拉取相关更新。

总体来看，本周的讨论主要集中在补丁的应用和后续管理上，参与者们积极协作，确保补丁的顺利整合。

#### 📝 邮件列表

1. **[08-27 10:43]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
2. **[08-27 05:57]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-27 14:08]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-27 15:11]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
5. **[08-27 14:14]** Re: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 22 Aug 2025 11:18:53 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在允许处理影子阶段 2 的读取权限故障。补丁的核心内容是，当处理影子阶段 2 的故障时，允许继续处理读取故障，而不是直接返回错误。

在历史讨论中，Wei-Lin Chang 提出了补丁的背景，指出在使用影子映射时，阶段 2 的权限可能与阶段 1 不一致，因此需要处理读取权限故障。Oliver Upton 和 Marc Zyngier 对此进行了积极的反馈，认为补丁的思路是正确的，并讨论了与 MMU 故障相关的架构特性（如 FEAT_ETS3）。

在本周的新讨论中，Wei-Lin Chang 对 Marc Zyngier 提出的关于 W 位的疑问进行了回应，表示将准备补丁的另一个版本以澄清相关内容。同时，他也与 Oliver Upton 讨论了 ETS 特性，并表示会在下一个版本中进行调整。整体来看，本周的讨论主要集中在补丁细节的澄清和版本更新的准备上。

#### 📝 邮件列表

1. **[08-22 11:18]** [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-22 02:25]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[08-22 10:40]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-26 21:49]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
5. **[08-26 21:55]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 11: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 25 Aug 2025 10:39:50 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 HiSilicon 的 HIP10 和 HIP10C 处理器的 erratum 162200802 提出的补丁（PATCH v2 0/4）。该补丁主要包括四个部分，旨在解决与虚拟处理单元（vPE）调度相关的硬件缺陷。

在历史讨论中，补丁的第一版（V1）已提出了对 GICD.num_LPIs 可写支持的需求，但存在一些错误和不足之处，特别是 erratum 编号的错误。此次 V2 版本修正了这些问题，并增加了对 GICD_TYPER.num_LPIs 的可写描述。

本周的新讨论中，Zhou Wang 提出了四个补丁的具体实现：
1. **补丁 1**：允许用户空间写入 GICD_TYPER.num_LPIs，默认值为 0。
2. **补丁 2**：增加了对 GICD.num_LPIs 的自测用例，确保在 GIC 初始化前可以修改该值，但初始化后不可更改。
3. **补丁 3**：更新文档，详细描述 GICD_TYPER.num_LPIs 的可写性。
4. **补丁 4**：为 HIP10/HIP10C 的 erratum 162200802 添加了工作区，限制 vLPIs 的数量，以避免调度命令超时的问题。

整体来看，本周的讨论集中在补丁的具体实现和测试上，确保解决方案的有效性和文档的准确性。

#### 📝 邮件列表

1. **[08-25 10:39]** [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[08-25 10:39]** [PATCH v2 1/4] KVM: arm64: Allow userspace to write GICD_TYPER.num_LPIs
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[08-25 10:39]** [PATCH v2 2/4] KVM: arm64: selftests: Add test for GICD.num_LPIs
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[08-25 10:39]** [PATCH v2 3/4] Documentation: KVM: arm64: Add GICD_TYPER.num_LPIs writable description
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
5. **[08-25 10:39]** [PATCH v2 4/4] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 12: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 20 Aug 2025 15:55:20 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 在 KVM 中的支持，主要集中在一个补丁系列（PATCH v10 00/43）上。该补丁旨在允许在 KVM 下运行受保护的虚拟机，相关的来宾支持已在 v6.14-rc1 中合并。

在历史讨论中，Steven Price 提到补丁系列中修复了一些问题，包括在领域销毁时主机遍历阶段 2 页表的潜在问题。此外，补丁还处理了 Granule Protection Faults (GPFs)，确保当主机尝试访问已委托给领域的 granules 时能够正确捕获并触发故障。

在本周的新讨论中，Catalin Marinas 对补丁中的 GPF 处理提出了建议，认为无论故障发生在 EL0 还是 EL1，最终结果是相似的。他建议可以简化代码，直接返回 1，避免调用 arm64_notify_die()，让 do_mem_abort() 处理内核故障与用户信号的区别，并提到使用 die_kernel_fault() 时会打印更多信息。

总体而言，讨论集中在如何优化和简化补丁的实现，以提高代码的可读性和效率。

#### 📝 邮件列表

1. **[08-20 15:55]** [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[08-20 15:55]** [PATCH v10 02/43] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
3. **[08-29 12:38]** Re: [PATCH v10 02/43] arm64: RME: Handle Granule Protection Faults
 (GPFs)
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 13: [PATCH v4 06/23] perf: arm_pmuv3: Keep out of guest counter partition

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 30 Aug 2025 04:13:39 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM PMU v3 的补丁（patch），其目的是在虚拟化环境中避免访客（guest）计数器的分区干扰。补丁的编号为 v4 06/23，具体内容涉及如何处理性能计数器，以确保在虚拟机中运行时，不会影响到计数器的准确性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是基于之前对 ARM PMU v3 性能计数器管理的讨论而提出的，目的是提升虚拟化性能并确保计数器的独立性。

在本周的新讨论中，参与者 Colton Lewis 提出了对补丁代码的具体修改建议，指出某一行代码应使用“|=”操作符。这表明在补丁的实现细节上仍存在需要进一步调整的地方，可能影响到补丁的最终效果。

总结而言，此次讨论集中在如何优化 ARM PMU v3 的性能计数器管理上，尽管补丁已提交，但仍需根据反馈进行必要的修改。

#### 📝 邮件列表

1. **[08-30 04:13]** Re: [PATCH v4 06/23] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH 00/16] KVM: arm64: Add "struct kvm_page_fault"

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 21 Aug 2025 14:00:26 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构引入一个新的结构体 "struct kvm_page_fault" 的提案。该提案旨在简化处理错误路径的代码，并为未来的 KVM Userfault 功能铺平道路。

在历史讨论中，Sean Christopherson 提出了这个 RFC（请求反馈的补丁），强调通过引入 kvm_page_fault 结构体，可以减少传递给辅助函数的参数数量，并为架构无关的 KVM 代码提供更好的支持。Oliver Upton 也参与了讨论，提出了一些关于如何更好地表示和命名结构体字段的建议。

在本周的新讨论中，参与者们继续探讨如何将 kvm_page_fault 结构体与现有的错误状态寄存器（ESR）接口结合使用。Sean Christopherson 表达了对使用 ESR 作为架构视角的真实来源的兴趣，并讨论了在架构无关代码中实现这一点的复杂性。Oliver Upton 提出了在当前阶段保留某些字段（如 exec、write 和 is_perm），同时为访问 kvm_page_fault 添加适当的 API，以便在不影响通用代码的情况下逐步转换。这种方法可以让 KVM 的通用功能开始基于 kvm_page_fault 构建，同时 arm64 可以独立进行相关的转换工作。整体来看，讨论集中在如何平衡架构特定代码与通用代码之间的关系，以及如何有效地推进补丁的实现。

#### 📝 邮件列表

1. **[08-21 14:00]** [RFC PATCH 00/16] KVM: arm64: Add "struct kvm_page_fault"
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-21 14:00]** [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault" for
 tracking abort state
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-21 15:31]** Re: [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault"
 for tracking abort state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[08-26 11:58]** Re: [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault"
 for tracking abort state
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-26 12:29]** Re: [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault"
 for tracking abort state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[08-26 14:29]** Re: [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault"
 for tracking abort state
   - 发件人: Sean Christopherson <seanjc@google.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] [kvm?] WARNING: locking bug in vgic_put_irq

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 25 Aug 2025 14:08:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM (Kernel-based Virtual Machine) 中的一个锁定错误，具体涉及 `vgic_put_irq` 函数。syzbot 在最近的测试中发现了一个警告，指示在处理虚拟化中断时出现了锁定问题。

在历史讨论中，虽然没有具体的补丁或详细的背景信息，但可以推测该问题与 KVM 的 ARM64 实现有关，尤其是在处理虚拟化中断时的锁定机制。邮件中提供了相关的错误信息和调用栈，显示了在 `vgic_put_irq` 函数中尝试获取锁时的上下文问题。

本周的新讨论主要集中在 syzbot 报告的警告信息上，指出在特定的内核版本（7b8346bd9fce）中，存在无效的等待上下文。报告中详细列出了当前持有的锁和调用栈，帮助开发者定位问题。syzbot 还建议如果有人修复了该问题，请在提交的补丁中添加相应的报告标签。

总体而言，本周的讨论强调了 KVM ARM64 实现中的锁定问题，并呼吁开发者关注并解决这一潜在的错误。

#### 📝 邮件列表

1. **[08-25 14:08]** [syzbot] [kvmarm?] [kvm?] WARNING: locking bug in vgic_put_irq
   - 发件人: syzbot <syzbot+cef594105ac7e60c6d93@syzkaller.appspotmail.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 changes for 6.17, take #2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 28 Aug 2025 13:00:10 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.17 版本中的变更，主要由 Oliver Upton 提出并更新了相关补丁。

1. **原始补丁内容**：Oliver 提交了一系列修复，旨在解决 KVM/arm64 中关于 CPU 系统寄存器处理的多个问题，特别是针对受保护虚拟机的系统寄存器处理和 VNCR 数据中断的改进。这些修复包括对 FEAT_RAS 功能的支持、虚拟机销毁时的页表处理以及 AT S12 模拟的修复等。

2. **之前讨论要点**：虽然本线程没有详细的历史讨论记录，但可以推测之前的讨论集中在 KVM/arm64 的稳定性和性能改进上，特别是系统寄存器的处理和虚拟机的上下文管理。

3. **本周的新讨论与进展**：在本周的讨论中，Oliver 提交了包含多个修复的补丁，并表示由于工作原因延误了提交。Paolo Bonzini 对此表示接受，并提到他在拉取请求中添加了额外的上下文信息。整体来看，本周的讨论主要围绕补丁的内容和提交的确认，标志着 KVM/arm64 在即将发布的 6.17 版本中将进行重要的修复和改进。

#### 📝 邮件列表

1. **[08-28 13:00]** [GIT PULL] KVM/arm64 changes for 6.17, take #2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[08-29 19:41]** Re: [GIT PULL] KVM/arm64 changes for 6.17, take #2
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

