# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 12:44:39

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 154
- **总 Thread 数**: 26
- **大型 Thread** (>20封): 1 个

### 分类分布

- **PATCH**: 20 threads (114 邮件)
- **RFC**: 2 threads (23 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Discussion**: 1 threads (4 邮件)
- **Other**: 2 threads (12 邮件)

---

## 📌 PATCH

共 20 个 thread

---

### Thread 1: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 32 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 24 Sep 2025 16:10:40 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于为 `guest_memfd` 实现直接映射移除支持的补丁系列（PATCH v7 00/12）。该补丁旨在通过从主机内核的直接映射中取消虚拟机客体内存的映射，以减轻类似 Spectre 的瞬态执行问题。补丁系列的核心是扩展 `guest_memfd` 的功能，使其能够在 KVM 客户机中实现这种保护。

在历史讨论中，参与者们讨论了补丁的设计和实现细节，包括如何处理直接映射状态、TLB 刷新、以及在不同架构下的支持情况。补丁中引入了 `AS_NO_DIRECT_MAP` 标志，以标识不在直接映射中的映射类型，并对现有的 `secretmem` 进行了一些优化。

本周的新讨论中，Patrick Roy 提出了多个补丁，主要包括：
1. **导出函数**：为 KVM 模块导出 `set_direct_map_valid_noflush` 和 `flush_tlb_kernel_range` 函数，以支持直接映射的移除和 TLB 刷新。
2. **添加标志**：为 `KVM_CREATE_GUEST_MEMFD()` ioctl 添加 `GUEST_MEMFD_FLAG_NO_DIRECT_MAP` 标志，以便在创建 `guest_memfd` 时移除直接映射。
3. **模块参数**：引入模块参数以选择性禁用 TLB 刷新，旨在提高性能，但也引发了关于安全性的讨论。
4. **自测**：更新自测代码以覆盖新功能，确保在直接映射移除的情况下，客体内存仍能正常工作。

参与者们对补丁的设计和实现进行了积极的反馈和建议，讨论了不同架构的支持情况及其潜在影响，确保补丁在功能和性能上的平衡。

#### 📝 邮件列表

1. **[09-24 16:10]** [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Patrick Roy <patrick.roy@campus.lmu.de>
2. **[09-24 16:10]** [PATCH v7 01/12] arch: export set_direct_map_valid_noflush to KVM module
   - 发件人: Patrick Roy <patrick.roy@campus.lmu.de>
3. **[09-24 16:10]** [PATCH v7 02/12] x86/tlb: export flush_tlb_kernel_range to KVM module
   - 发件人: Patrick Roy <patrick.roy@campus.lmu.de>
4. **[09-24 16:10]** [PATCH v7 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Patrick Roy <patrick.roy@campus.lmu.de>
5. **[09-24 15:22]** [PATCH v7 04/12] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
6. **[09-24 15:22]** [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
7. **[09-24 15:22]** [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling TLB
 flushing
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
8. **[09-24 15:22]** [PATCH v7 07/12] KVM: selftests: load elf via bounce buffer
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
9. **[09-24 15:22]** [PATCH v7 08/12] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
10. **[09-24 15:22]** [PATCH v7 09/12] KVM: selftests: Add guest_memfd based
 vm_mem_backing_src_types
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
11. **[09-24 15:22]** [PATCH v7 10/12] KVM: selftests: cover GUEST_MEMFD_FLAG_NO_DIRECT_MAP
 in existing selftests
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
12. **[09-24 15:22]** [PATCH v7 11/12] KVM: selftests: stuff vm_mem_backing_src_type into
 vm_shape
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
13. **[09-24 15:22]** [PATCH v7 12/12] KVM: selftests: Test guest execution from direct map
 removed gmem
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
14. **[09-24 15:29]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
15. **[09-24 17:38]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: David Hildenbrand <david@redhat.com>
16. **[09-25 12:25]** Re: [PATCH v7 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
17. **[09-25 12:26]** Re: [PATCH v7 04/12] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: David Hildenbrand <david@redhat.com>
18. **[09-25 13:00]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: David Hildenbrand <david@redhat.com>
19. **[09-25 13:02]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
20. **[09-25 15:50]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
21. **[09-25 15:52]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
22. **[09-25 11:27]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Dave Hansen <dave.hansen@intel.com>
23. **[09-25 21:20]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
24. **[09-25 21:28]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: David Hildenbrand <david@redhat.com>
25. **[09-25 21:32]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
26. **[09-25 12:59]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Dave Hansen <dave.hansen@intel.com>
27. **[09-25 22:13]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
28. **[09-26 10:46]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Patrick Roy <patrick.roy@linux.dev>
29. **[09-26 11:53]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for
 disabling TLB flushing
   - 发件人: Will Deacon <will@kernel.org>
30. **[09-26 15:49]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Patrick Roy <patrick.roy@linux.dev>
31. **[09-26 22:09]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
32. **[09-27 08:38]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Patrick Roy <patrick.roy@linux.dev>

---

### Thread 2: [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Sat, 20 Sep 2025 20:51:58 +0100

#### 🤖 AI 总结

本邮件线程主要讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上的自测和功能改进。

1. **原始 patch/问题的内容**：
   Mark Brown 提出的补丁（PATCH 0/2）旨在增强 KVM 的自测功能，特别是为 `set_id_regs` 函数增加对 `ID_AA64ISAR3_EL1` 的覆盖。该补丁还包括对测试代码的维护性改进。

2. **之前的讨论要点**：
   在历史讨论中，Mark 指出现有的自测缺乏对 `ID_AA64ISAR3_EL1` 的覆盖，这可能会影响 KVM 客户端的功能。补丁的应用依赖于之前的 `FEAT_LSFE` 变更。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Oliver Upton 和 Marc Zyngier 对补丁进行了审查并表示支持，补丁已被应用到后续版本中。Marc Zyngier 提出了对补丁基础提交的疑问，指出所引用的提交在其环境中不可用。Oliver Upton 还提出了其他补丁，旨在解决 KVM 在处理 MDSCR_EL1 和 ZCR_EL2 时的性能问题，并确保在嵌套环境中正确处理 SVE 异常。这些补丁也得到了审查并被应用。

整体来看，本周的讨论集中在补丁的审查、应用及其对 KVM 性能的影响上，显示出开发者们对改进 KVM 功能的持续关注。

#### 📝 邮件列表

1. **[09-20 20:51]** [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-22 16:35]** Re: [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-24 19:29]** Re: [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in set_id_regs
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-24 19:38]** Re: [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in set_id_regs
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-24 16:51]** [PATCH 0/2] KVM: arm64: nv: FGT traps of MDSCR_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-24 16:51]** [PATCH 1/2] KVM: arm64: Compute per-vCPU FGTs at vcpu_load()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-24 16:51]** [PATCH 2/2] KVM: arm64: nv: Use FGT write trap of MDSCR_EL1 when available
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-25 12:09]** Re: [PATCH 1/2] KVM: arm64: Compute per-vCPU FGTs at vcpu_load()
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[09-25 12:12]** Re: [PATCH 2/2] KVM: arm64: nv: Use FGT write trap of MDSCR_EL1 when
 available
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[09-25 12:12]** Re: [PATCH 0/2] KVM: arm64: selftests: Cover ID_AA64ISAR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[09-26 12:41]** [PATCH 0/2] KVM: arm64: Fixes for NV+SVE
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-26 12:41]** [PATCH 1/2] KVM: arm64: nv: Don't treat ZCR_EL2 as a 'mapped' register
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-26 12:41]** [PATCH 2/2] KVM: arm64: nv: Don't advance PC when pending an SVE exception
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[09-27 12:29]** Re: [PATCH 0/2] KVM: arm64: Fixes for NV+SVE
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 9 Sep 2025 15:12:45 +0100

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下如何将 MMIO（内存映射 I/O）捐赠给虚拟机监控器（hypervisor）。原始的 patch 提出了在处理 MMIO 时，确保 pfn（页面帧号）确实是 MMIO，并且由 hypervisor 拥有，同时确保主机没有在该 pfn 上映射其他内容。

在历史讨论中，参与者提出了多个问题和建议，主要集中在如何确保代码的安全性和可靠性，特别是在错误处理和初始化顺序方面。Mostafa Saleh 和 Will Deacon 讨论了在 hypervisor 启动时如何处理 MMIO 页面的映射，以及在不同情况下的初始化顺序。

在本周的新讨论中，Mostafa Saleh 强调了当前方法的优越性，认为在 KVM 初始化失败时，SMMU（系统内存管理单元）仍应能够探测并保持系统运行。Jason Gunthorpe 建议将 pkvm 驱动绑定到特定的 pkvm 设备驱动上，以简化处理逻辑。Will Deacon 则表示希望在 donation 函数中添加检查，以避免调用者遗漏必要的检查。

总体来看，本周的讨论进一步深化了对 patch 的理解，并提出了如何优化驱动程序处理逻辑的建议。

#### 📝 邮件列表

1. **[09-09 15:12]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-09 15:42]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-12 14:54]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-16 13:27]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[09-16 14:24]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[09-23 14:35]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[09-23 14:38]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
8. **[09-26 15:33]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Will Deacon <will@kernel.org>
9. **[09-26 15:42]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 4: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64

**📧 邮件数**: 9 | **👥 参与者**: 6 | **📅 开始时间**: Mon, 22 Sep 2025 13:24:52 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 arm64 的 KVM_TRANSLATE ioctl 实现的补丁。该补丁旨在将访客虚拟地址（GVA）转换为访客物理地址（GPA），并支持 VHE 和非 VHE 配置。补丁中包含了对相关代码的修改和自测试用例的添加。

在历史讨论中，补丁的提出者 Priscilla Lam 解释了该补丁的动机，指出它可以帮助用户空间的虚拟机监控器（VMM）处理非 ISV 访客故障。该补丁的实现方式引起了参与者的关注，特别是对现有页面表遍历机制的忽视以及对复杂架构特性的处理不当。

本周的新讨论中，参与者 Oliver Upton 和 Marc Zyngier 提出了对补丁的多项批评，认为补丁未能充分利用内核中已有的翻译基础设施，并对补丁的设计和实现提出了疑问。Priscilla 对反馈表示感谢，并承诺将在后续版本中进行改进，包括使用共享的 S1 页面表遍历器和调整命名方式。最终，Priscilla 决定放弃当前的 KVM_TRANSLATE 实现，寻求其他解决方案。

综上所述，该补丁的讨论反映了对 arm64 虚拟化支持的深入探讨，以及在实现过程中需要考虑的架构复杂性和现有基础设施的有效利用。

#### 📝 邮件列表

1. **[09-22 13:24]** [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Priscilla Lam <prl@amazon.com>
2. **[09-22 16:27]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-23 09:03]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-23 01:29]** Re: Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Priscilla Lam <prl@amazon.com>
5. **[09-23 10:39]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Alexander Graf <graf@amazon.com>
6. **[09-23 10:02]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: David Woodhouse <dwmw2@infradead.org>
7. **[09-23 10:25]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-23 18:05]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Christoffer Dall <Christoffer.Dall@arm.com>
9. **[09-24 22:21]** Re: [PATCH] KVM: arm64: Implement KVM_TRANSLATE ioctl for arm64
   - 发件人: Priscilla Lam <prl@amazon.com>

---

### Thread 5: [PATCH v9 0/6] support FEAT_LSUI and apply it on futex atomic ops

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 22 Sep 2025 11:22:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Armv9.6 的 FEAT_LSUI 特性的补丁集，该特性允许特权级代码在不清除 PSTATE.PAN 位的情况下访问用户内存。补丁集共包含六个部分，主要集中在 futex 原子操作的实现上。

历史讨论部分提到，补丁从 v8 版本到 v9 进行了多次重构和修改，主要包括对原有 futex 原子操作的重构，以便在新的 FEAT_LSUI 特性下进行优化。补丁的主要内容包括添加 CPU 特性检测、将 FEAT_LSUI 暴露给虚拟机、更新 Kconfig 以检测工具链支持、重构原子操作实现等。

在本周的新讨论中，Yeoreum Yun 提出了补丁的具体实现，强调了如何利用 FEAT_LSUI 来简化原子操作的实现。补丁的具体内容包括：
1. 添加 FEAT_LSUI 的 CPU 特性检测。
2. 将 FEAT_LSUI 暴露给 KVM 虚拟机。
3. 更新 Kconfig 以检测工具链支持。
4. 重构 futex 原子操作以适应 FEAT_LSUI。
5. 实现使用 FEAT_LSUI 的 futex 原子操作。

此外，参与者 Mark Brown 提到需要将相关功能添加到 set_id_regs 中，并表示将为此提供补丁。Yeoreum Yun 也表示会补充 kselftest 功能以进行测试。整体来看，讨论集中在如何有效利用新特性以提升内核性能和功能上。

#### 📝 邮件列表

1. **[09-22 11:22]** [PATCH v9 0/6] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[09-22 11:22]** [PATCH v9 1/5] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-22 11:22]** [PATCH v9 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-22 11:22]** [PATCH v9 3/5] arm64: Kconfig: Detect toolchain support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-22 11:22]** [PATCH v9 4/5] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[09-22 11:22]** [PATCH v9 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[09-22 12:25]** Re: [PATCH v9 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[09-22 15:49]** Re: [PATCH v9 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[09-23 10:28]** Re: [PATCH v9 2/5] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 6: [PATCH kvmtool v4 0/7] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 24 Sep 2025 14:45:04 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的多个补丁（PATCH），这是 kvmtool v4 版本的更新。

1. **原始补丁内容**：该补丁系列旨在为 ARM64 架构添加嵌套虚拟化支持，允许虚拟 CPU 在 EL2 模式下运行。补丁包括更新内核头文件以支持新功能、添加命令行选项以启动嵌套虚拟机、设置维护 IRQ、支持计数器偏移控制、以及处理 virtio 的字节序问题等。

2. **之前讨论要点**：在之前的讨论中，参与者们对嵌套虚拟化的实现进行了多次迭代，主要集中在如何有效地管理 IRQ、时钟中断以及确保兼容性等方面。Marc Zyngier 和 Andre Przywara 是主要的贡献者，他们对补丁进行了多次修改和优化。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现细节上，包括：
   - 新增了 `--nested` 命令行选项以启动 VCPU 在 EL2 模式。
   - 通过 VGIC 设备属性设置维护 IRQ，并确保其符合平台规范。
   - 添加了 `--counter-offset` 选项以控制全局计数器偏移。
   - 引入了 `--e2h0` 选项以支持不需要 VHE 的旧版来宾。
   - 处理了在嵌套虚拟化下 virtio 的字节序重置问题。

整体来看，讨论围绕着如何提高 ARM64 嵌套虚拟化的功能和稳定性展开，补丁的实施将进一步增强 kvmtool 的能力。

#### 📝 邮件列表

1. **[09-24 14:45]** [PATCH kvmtool v4 0/7] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[09-24 14:45]** [PATCH kvmtool v4 1/7] Sync kernel UAPI headers with v6.16
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[09-24 14:45]** [PATCH kvmtool v4 2/7] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[09-24 14:45]** [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[09-24 14:45]** [PATCH kvmtool v4 4/7] arm64: Add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[09-24 14:45]** [PATCH kvmtool v4 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[09-24 14:45]** [PATCH kvmtool v4 6/7] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
8. **[09-24 14:45]** [PATCH kvmtool v4 7/7] arm64: Handle virtio endianness reset when running nested
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 7: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 19 Sep 2025 16:50:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM (Kernel-based Virtual Machine) 的补丁，主要关注在 arm64 架构下对 pKVM 内存转换的范围参数进行检查。补丁的目的是在大多数 pKVM 内存转换中增加对主机发出的范围的验证，以防止后续的边界溢出问题。

在历史讨论中，Vincent Donnefort 提出了补丁的初步版本，指出当前缺乏对范围参数的验证可能导致安全隐患。Marc Zyngier 对此补丁提出了建议，强调需要将边界检查改为包含结束范围，以避免合法范围被错误地判定为无效。

在本周的新讨论中，Vincent Donnefort 和其他参与者继续探讨边界检查的细节。Marc Zyngier 提出，某些范围可能会导致后续检查的风险，Oliver Upton 则表示希望这些范围检查尽可能少地依赖于特定的地址空间假设。讨论中还提到，如果不包括结束边界，可能会导致检查被绕过的风险，进一步强调了补丁的重要性。

总体来看，本周的讨论围绕补丁的实现细节和潜在风险展开，参与者们对如何确保范围检查的有效性进行了深入的探讨。

#### 📝 邮件列表

1. **[09-19 16:50]** [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[09-21 12:29]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-22 22:00]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[09-22 16:33]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-23 10:18]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 8: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 19 Sep 2025 16:52:55 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 HIP10/HIP10C 的 erratum 162200802 提出的补丁（PATCH v2 0/4），旨在为该硬件缺陷提供解决方案。

在历史讨论中，Marc Zyngier 表达了对在用户空间暴露问题的担忧，建议首先在 GIC（通用中断控制器）层面制定解决策略，而不是直接向用户空间开放。Zhou Wang 也提到需要明确解决方案，以避免在内核中引入新用户空间 ABI。

在本周的新讨论中，Zhou Wang 提出可以先合并该补丁，然后再继续解决之前提到的问题。对此，Marc Zyngier 反驳道，补丁引入了新的用户空间 ABI，这是不可接受的，尤其是当有其他有效的解决方案（如不启用 GICv4）时。他对当前的实现表示不满，认为这些实现存在严重问题，不值得挽救，并建议使用现有的有效解决方案来保持虚拟机的运行。

最后，Zhou Wang 进一步澄清，HIP09/10/10C 支持 GICv4.0 和 GICv4.1，可以通过 BIOS 开关进行选择。整体来看，讨论围绕如何有效解决硬件缺陷而展开，双方对补丁的接受度和解决方案的有效性存在分歧。

#### 📝 邮件列表

1. **[09-19 16:52]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-26 15:15]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[09-26 09:57]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-26 19:28]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 9: [PATCH v10 31/43] arm_pmu: Provide a mechanism for disabling the
 physical IRQ

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 22 Sep 2025 10:03:07 +1000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM PMU（性能监控单元）的补丁，具体是提供一种机制来禁用物理 IRQ（中断请求）。该补丁是 v10 版本中的第 31 个补丁，旨在改善 ARM 架构在虚拟化环境中的性能监控能力。

在之前的讨论中，虽然没有详细记录，但可以推测该补丁的提出是为了应对 ARM 架构在 KVM（内核虚拟机）中对性能监控的需求，尤其是在支持新的硬件特性时。

本周的新讨论中，Gavin Shan 对该补丁进行了审核并表示认可，确认其符合要求。此外，Emi Kisanuki 报告了在 Fujitsu 的内部模拟器上测试该补丁的结果，成功启动了 realm VM，并且除了 PMU 测试外，其他 kvm-unit-tests 测试均通过。Steven Price 对 Emi 的测试结果表示感谢，显示出团队对补丁进展的积极反馈。

总体来看，该补丁在社区中获得了积极的审查和测试反馈，显示出其在 ARM 虚拟化支持中的重要性和有效性。

#### 📝 邮件列表

1. **[09-22 10:03]** Re: [PATCH v10 31/43] arm_pmu: Provide a mechanism for disabling the
 physical IRQ
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[09-22 10:03]** Re: [PATCH v10 32/43] arm64: RME: Enable PMU support with a realm
 guest
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[09-24 02:34]** RE: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
4. **[09-26 10:10]** Re: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 10: [PATCH] KVM: selftests: Track width of arm64's timer counter as
 "int", not "uint64_t"

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 26 Sep 2025 08:58:38 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的自测试补丁，主要内容是将 arm64 的定时器计数器宽度从 "uint64_t" 修改为 "int"。这一修改旨在解决 clang 编译器在类型不匹配时产生的错误，特别是在使用 clamp 函数时，导致的指针类型比较错误。

在历史讨论中，补丁的背景是由 Sean Christopherson 提出的，目的是修复在处理定时器计数器宽度时出现的类型问题。具体来说，ilog2() 函数返回的是 "int"，而使用 "uint64_t" 会引发编译警告，影响代码的可编译性。

在本周的新讨论中，Oliver Upton 对该补丁进行了审查并表示支持，认为补丁解决了问题。Marc Zyngier 随后确认已将该补丁应用于修复分支，并感谢 Sean 的贡献。最终，该补丁被成功合并，标志着这一问题的解决。

#### 📝 邮件列表

1. **[09-26 08:58]** [PATCH] KVM: selftests: Track width of arm64's timer counter as
 "int", not "uint64_t"
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[09-26 12:48]** Re: [PATCH] KVM: selftests: Track width of arm64's timer counter as
 "int", not "uint64_t"
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-27 12:29]** Re: [PATCH] KVM: selftests: Track width of arm64's timer counter as "int", not "uint64_t"
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 11: [PATCH] KVM: arm64: selftests: Test effective value of HCR_EL2.AMO

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 26 Sep 2025 15:44:54 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试，主要关注 HCR_EL2.AMO 的有效值测试。

1. **原始 patch/问题的内容**：Oliver Upton 提交的补丁旨在解决一个架构缺陷，允许在 HCR_EL2.{E2H, TGE} = {1, 0} 时将 AMO 视为 1。此补丁通过添加测试用例来验证在这种情况下是否能正确处理 SError 注入。

2. **之前的讨论要点**：本邮件线程没有提供历史讨论的内容，因此无法总结之前的讨论要点。

3. **本周的新讨论、进展或结论**：本周的讨论中，Oliver Upton 提交了补丁并详细描述了测试用例的实现，确保在特定条件下能够捕获 SError 异常。Marc Zyngier 随后确认已将该补丁应用于修复中，并表示感谢。这表明补丁得到了认可并将被纳入代码库中。

总体来看，本周的讨论集中在补丁的提交和确认上，强调了对 KVM 在 arm64 架构下的功能测试的重要性。

#### 📝 邮件列表

1. **[09-26 15:44]** [PATCH] KVM: arm64: selftests: Test effective value of HCR_EL2.AMO
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-27 12:30]** Re: [PATCH] KVM: arm64: selftests: Test effective value of HCR_EL2.AMO
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH] KVM: arm64: Use the in-context stage-1 in __kvm_find_s1_desc_level()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 26 Sep 2025 15:42:46 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“在 __kvm_find_s1_desc_level() 中使用上下文阶段 1”。该补丁旨在解决在 EL2 级别运行 external_aborts 自测时出现的错误，原因是该函数硬编码为 EL1&0 模式，导致在遍历上下文时阶段 1 MMU 被禁用。

历史讨论中没有提供具体的背景信息，但本周的讨论集中在补丁的具体实现上。Oliver Upton 提出了补丁，修改了 __kvm_find_s1_desc_level() 函数，以根据当前 vCPU 的上下文选择适当的翻译模式。具体来说，如果 vCPU 处于 HYP 上下文，则使用 EL2 或 EL20 模式，否则使用 EL10 模式。

在本周的新讨论中，Marc Zyngier 对补丁表示认可，并确认已将其应用于修复中。补丁的提交标识为 fcaa3f59fda3579ee77127abbc58896c67c36cab，标志着该问题得到了有效解决。

#### 📝 邮件列表

1. **[09-26 15:42]** [PATCH] KVM: arm64: Use the in-context stage-1 in __kvm_find_s1_desc_level()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-27 12:30]** Re: [PATCH] KVM: arm64: Use the in-context stage-1 in __kvm_find_s1_desc_level()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH] kvm, selftests: ioctl to handle MSIs injected from userspace as software-bypassing vLPIs

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 25 Sep 2025 11:01:16 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中处理来自用户空间的中断（MSI）注入的补丁。该补丁旨在通过实现一个新的 ioctl 接口（KVM_DEBUG_GIC_MSI_SETUP），使得用户空间能够直接将 MSI 注入到虚拟化环境中，绕过软件处理，从而实现对 GICv4 直接 vLPI（虚拟本地外部中断）的测试。

在历史讨论中，没有提供具体的背景信息，但本周的讨论中，Maximilian Dittgen 提出了该补丁的实现细节，包括如何通过 ioctl 创建 IRQ 路由表条目，并设置 ITS（中断翻译服务）结构，以便将 MSI 映射到 vLPI。此外，他还在自测代码中实现了一个 -D 标志，以便使用直接 vLPI 注入进行压力测试。

Marc Zyngier 对该补丁提出了质疑，认为注入中断的方式过于复杂，并建议可以通过其他方法实现相同的测试效果，而不需要增加内核代码。他提到可以模拟恢复有待处理中断的虚拟机，或者使用已有的中断注入机制来实现。

总的来说，本周的讨论围绕补丁的实现细节和可行性展开，提出了不同的测试策略和实现方式。

#### 📝 邮件列表

1. **[09-25 11:01]** [PATCH] kvm, selftests: ioctl to handle MSIs injected from userspace as software-bypassing vLPIs
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
2. **[09-25 10:25]** Re: [PATCH] kvm, selftests: ioctl to handle MSIs injected from userspace as software-bypassing vLPIs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] KVM: arm64: selftests: Cope with arch silliness in EL2 selftest

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 23 Sep 2025 10:30:06 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试补丁，主题为“处理 EL2 自测试中的架构问题”。 

**原始补丁内容**：补丁由 Oliver Upton 提出，旨在解决在 HCR_EL2.TID3 设置时，某些实现未能正确处理 ID 寄存器空间的问题。具体来说，缺少 FEAT_FGT 特性的实现不需要在此情况下捕获整个 ID 寄存器空间，这可能导致虚拟机无法正确识别特性缺失。补丁通过在缺少 FEAT_FGT 时接受零值来应对不合作的实现。

**之前讨论要点**：在历史讨论中并未提供具体的背景信息，但可以推测该补丁是基于之前的自测试系列进行的改进。

**本周新讨论及进展**：本周，Oliver Upton 提交了补丁，并在邮件中说明了补丁的实现细节。Marc Zyngier 随后确认已将该补丁应用到下一个版本中，并表示感谢。这表明补丁得到了认可并将进入后续的开发流程。

#### 📝 邮件列表

1. **[09-23 10:30]** [PATCH] KVM: arm64: selftests: Cope with arch silliness in EL2 selftest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-24 19:38]** Re: [PATCH] KVM: arm64: selftests: Cope with arch silliness in EL2 selftest
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Sep 2025 14:20:30 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测功能的改进，特别是如何在 VHE EL2（Virtualization Host Extensions Exception Level 2）环境中运行自测。

**原始 patch/问题的内容**：
Oliver Upton 提出了一个补丁系列（共13个补丁），旨在将现有的自测基础设施移植到 VHE EL2 环境中，以便更有效地测试一些与内存管理单元（MMU）相关但未被 KVM 使用的功能。补丁中强调了创建 VGICv3（虚拟通用中断控制器）的必要性，以支持 EL2 的启用。

**之前讨论要点**：
在历史讨论中，Oliver 提到需要在补丁中加入默认的 VGICv3，并承认之前与 Sean 的讨论中对这一点的看法有所改变。这一补丁的提出是为了应对测试中的一些挑战。

**本周的新讨论、进展或结论**：
在本周的讨论中，Marc Zyngier 确认了 Oliver 的补丁已被应用到下一个开发版本中，并列出了每个补丁的具体提交信息。这表明补丁系列得到了认可并将继续推进，标志着在 VHE EL2 环境下的自测功能正在逐步完善。

#### 📝 邮件列表

1. **[09-17 14:20]** [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-24 19:37]** Re: [PATCH 00/13] KVM: arm64: selftests: Run selftests in VHE EL2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt
 specifiers

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 23 Sep 2025 17:21:15 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中生成 HYP 定时器中断说明符的补丁（PATCH kvmtool v3 6/6）。该补丁旨在改进 KVM（Kernel-based Virtual Machine）在处理 HYP 定时器中断时的行为。

在之前的讨论中，参与者探讨了与 ARM 架构特性相关的细节，特别是 FEAT_E2H0 和 FEAT_VHE 的实现关系。Andre Przywara 提出，即使 FEAT_E2H0 被实现，FEAT_VHE 也应当被视为实现，这引发了对定时器行为的进一步讨论。他指出，相关的配置段落和伪代码并未提及 SCR_EL2.E2H0，而是直接与 FEAT_VHE 相关联。

在本周的新讨论中，Andre 再次强调了这一点，并指出这种写法并不意味着 ARMv8.0 是非法的，因为 E2H 在该版本中是保留位（RES0）。Marc Zyngier 补充说，这主要是 KVM 的一个缺陷，如果我们假设没有 VHE，那么 CNTHV_*_EL2 应该被定义为 UNDEF，这并不算大问题。

总体来看，本周的讨论进一步澄清了补丁的意图和与 ARM 架构特性的复杂关系，参与者们对如何处理这些特性达成了一定的共识。

#### 📝 邮件列表

1. **[09-23 17:21]** Re: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt
 specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[09-23 19:16]** Re: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 21 Sep 2025 06:22:56 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于对 arm64 架构中 TCR_EL1 字段宏的清理工作，涉及到的补丁为 [PATCH V5 0/4]。该补丁的主要内容是将分散在 arm64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏进行整理，更新所需的寄存器字段定义，并在 KVM 头文件中进行必要的替换。这一清理工作不会引入任何功能上的变化，主要目的是提升代码的整洁性和可维护性。

在历史讨论中，Anshuman Khandual 提出了该补丁，并详细说明了清理的背景和目的。补丁适用于 v6.17-rc6 版本，并且已经得到了相关人员的关注。

在本周的新讨论中，Will Deacon 确认已将补丁应用于 arm64 架构的 for-next/sysregs 分支，并感谢 Anshuman Khandual 的贡献。此外，他还提供了补丁中两个具体的更新链接，进一步推进了该清理工作的实施。整体来看，本周的讨论标志着该补丁的成功应用，推动了代码的整洁性提升。

#### 📝 邮件列表

1. **[09-21 06:22]** [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-22 14:14]** Re: [PATCH V5 0/4] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 18: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 26 Sep 2025 12:42:50 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中针对虚拟化性能监控单元（PMU）的一个补丁，具体为“[PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU MSRs for mediated vPMUs”。该补丁的目的是在某些情况下禁用对特定 PMU 寄存器的拦截，以优化虚拟化性能。

在之前的讨论中，参与者探讨了 AMD 处理器的一个特定情况：当客机中缺少全局 MSRs 时，客机仍然可以使用与主机能力相同数量的计数器。在这种情况下，RDPMC（Read Performance Monitoring Counters）拦截并不是在所有全局控制不可用的情况下都是必要的。

本周的讨论中，Sandipan Das 对此进行了回应，强调了在 AMD 处理器的特定情境下，确实可以不进行 RDPMC 的拦截。这表明补丁的设计考虑了不同处理器架构的特性，可能会进一步推动补丁的完善和应用。整体来看，本周的讨论为补丁的合理性提供了支持，并可能影响后续的开发方向。

#### 📝 邮件列表

1. **[09-26 12:42]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sandipan Das <sandidas@amd.com>

---

### Thread 19: [PATCH v8 08/12] perf: Add perf_event_attr::config4

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 25 Sep 2025 14:36:30 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH v8 08/12] perf: Add perf_event_attr::config4”，主要讨论了在 Linux 内核的性能监控（perf）模块中添加一个新的配置属性 `perf_event_attr::config4` 的补丁。

在历史讨论中，并未提供具体的背景信息，因此我们无法得知该补丁的详细内容或之前的讨论要点。

在本周的新讨论中，参与者 James Clark 向 Peter 询问是否有机会查看这个补丁。他提到之前的补丁（1-7）已经被接受，目前只在等待对 `config4` 变更的确认（ack），以便继续处理后续的补丁。这表明该补丁在整个补丁系列中是关键的一部分，且其接受与否将影响后续工作的进展。

总结而言，本周的讨论主要集中在对 `perf_event_attr::config4` 补丁的确认上，期待尽快得到反馈以推动后续补丁的处理。

#### 📝 邮件列表

1. **[09-25 14:36]** Re: [PATCH v8 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 20: [PATCH v3 00/15] KVM: Introduce KVM Userfault

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 23 Sep 2025 13:13:51 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）中引入 Userfault 功能的补丁（PATCH v3 00/15）。该补丁旨在增强 KVM 的内存管理能力，允许在用户空间处理页面故障，从而提高虚拟机的性能和灵活性。

在历史讨论中，虽然没有具体的邮件内容提供，但可以推测之前的讨论可能集中在 Userfault 功能的设计理念、实现细节以及其对现有 KVM 结构的影响。

本周的新讨论中，参与者 Nikita Kalyazin 回复了 Sean Christopherson，表示对补丁的认可，并询问 Sean 是否有时间尽快处理补丁的第二版（v2）。同时，Nikita 还提到定义和实现接口是否是该系列补丁的严格前提条件。这表明，当前讨论的重点在于补丁的后续开发计划和接口设计的重要性。

总体来看，讨论围绕 KVM Userfault 的实现进展展开，关注点在于如何进一步推动补丁的开发和接口的明确。

#### 📝 邮件列表

1. **[09-23 13:13]** Re: [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH 00/16] arm64: make alternative patching callbacks safe

**📧 邮件数**: 17 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 23 Sep 2025 18:48:47 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 架构的补丁系列，旨在确保内核代码中的替代补丁回调函数的安全性。Ada Couprie Diaz 提出了 16 个补丁，主要集中在优化和安全性方面。

1. **原始补丁/问题内容**：
   该补丁系列的目标是确保在补丁回调中使用的函数是安全的且不可被工具（如 KVM 和 Spectre 缓解）修改。补丁强调了当前回调函数可能在补丁应用过程中处于不一致状态，导致潜在的代码执行错误。

2. **之前讨论要点**：
   之前的讨论主要围绕如何标记回调函数为 `noinstr`，以避免它们被工具修改。补丁还提出了将某些函数标记为 `__always_inline` 以确保它们在编译时被内联，从而提高安全性。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Ada 提出了多个补丁，逐步实现了将多个回调函数标记为 `noinstr` 和 `__always_inline`，确保它们在补丁应用时不会被修改。特别是，补丁还引入了新的回调函数 `alt_cb_patch_ldr_to_ldar()`，用于将设备内存加载指令替换为加载获取指令，从而减小内核映像的大小。此外，Ada 还提出了一些开放性问题，寻求社区对如何处理错误消息和 `__init` 回调函数的看法。

总的来说，这一系列补丁旨在提高 ARM64 内核的安全性和稳定性，确保在补丁过程中不会引入潜在的错误。

#### 📝 邮件列表

1. **[09-23 18:48]** [RFC PATCH 00/16] arm64: make alternative patching callbacks safe
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
2. **[09-23 18:48]** [RFC PATCH 01/16] kasan: mark kasan_(hw_)tags_enabled() __always_inline
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
3. **[09-23 18:48]** [RFC PATCH 02/16] arm64: kasan: make kasan_hw_tags_enable() callback safe
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
4. **[09-23 18:48]** [RFC PATCH 03/16] arm64/insn: always inline aarch64_insn_decode_register()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
5. **[09-23 18:48]** [RFC PATCH 04/16] arm64/insn: always inline aarch64_insn_encode_register()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
6. **[09-23 18:48]** [RFC PATCH 05/16] arm64/insn: always inline aarch64_insn_encode_immediate()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
7. **[09-23 18:48]** [RFC PATCH 06/16] arm64/insn: always inline aarch64_insn_gen_movewide()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
8. **[09-23 18:48]** [RFC PATCH 07/16] arm64/proton-pack: make alternative callbacks safe
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
9. **[09-23 18:48]** [RFC PATCH 08/16] arm64/insn: always inline aarch64_insn_gen_logical_immediate()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
10. **[09-23 18:48]** [RFC PATCH 09/16] arm64/insn: always inline aarch64_insn_gen_add_sub_imm()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
11. **[09-23 18:48]** [RFC PATCH 10/16] arm64/insn: always inline aarch64_insn_gen_branch_reg()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
12. **[09-23 18:48]** [RFC PATCH 11/16] arm64/insn: always inline aarch64_insn_gen_extr()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
13. **[09-23 18:48]** [RFC PATCH 12/16] kvm/arm64: make alternative callbacks safe
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
14. **[09-23 18:49]** [RFC PATCH 13/16] arm64/insn: introduce missing is_store/is_load helpers
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
15. **[09-23 18:49]** [RFC PATCH 14/16] arm64/insn: always inline aarch64_insn_encode_ldst_size()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
16. **[09-23 18:49]** [RFC PATCH 15/16] arm64/insn: always inline aarch64_insn_gen_load_acq_store_rel()
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>
17. **[09-23 18:49]** [RFC PATCH 16/16] arm64/io: rework Cortex-A57 erratum 832075 to use callback
   - 发件人: Ada Couprie Diaz <ada.coupriediaz@arm.com>

---

### Thread 2: [RFC PATCH 0/5] Arm CCA planes support

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 26 Sep 2025 12:02:49 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm CCA（Confidential Compute Architecture）支持的补丁系列，主要集中在对多个执行环境的内存隔离支持上。

1. **原始补丁内容**：
   本系列补丁（RFC PATCH 0/5）旨在为 Arm CCA 引入“planes”概念，允许将一个领域划分为多个执行环境，并在这些环境之间实现内存隔离。补丁包括对 RMM（Realm Management Module）版本 1.1 的支持，涉及多个补丁文件，主要修改了 KVM 相关的代码。

2. **之前讨论要点**：
   在历史讨论中，补丁的背景和目标被阐明，强调了对 RMM v1.1 的支持以及如何在 Linux 中实现这一功能。补丁还提供了一个实验性的配置选项（RMM_V1_1），以便于测试新功能。

3. **本周的新讨论与进展**：
   本周的讨论包括多个补丁的具体实现细节：
   - **补丁 1**：添加了 RMM v1.1 中引入的新 SMC 定义。
   - **补丁 2**：处理辅助 RTT（Realm Translation Table）树的创建和销毁。
   - **补丁 3**：支持 S2AP（Stage 2 Address Permissions）更改的处理。
   - **补丁 4**：为每个辅助平面分配 PGD（Page Global Directory）和 VMID（Virtual Machine Identifier）。
   - **补丁 5**：引入了新的领域参数 `num_aux_planes` 和 `rtt_tree_pp`，分别定义辅助平面的数量和每个平面是否拥有独立的页表树。

这些补丁的实施将增强 Arm CCA 的功能，使得虚拟机管理程序能够更好地支持多平面架构的内存管理。

#### 📝 邮件列表

1. **[09-26 12:02]** [RFC PATCH 0/5] Arm CCA planes support
   - 发件人: Steven Price <steven.price@arm.com>
2. **[09-26 12:02]** [RFC PATCH 1/5] arm64: RME: Add SMC definitions introduced in RMM v1.1
   - 发件人: Steven Price <steven.price@arm.com>
3. **[09-26 12:02]** [RFC PATCH 2/5] arm64: RME: Handle auxiliary RTT trees
   - 发件人: Steven Price <steven.price@arm.com>
4. **[09-26 12:02]** [RFC PATCH 3/5] arm64: RME: Support RMI_EXIT_S2AP_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
5. **[09-26 12:02]** [RFC PATCH 4/5] arm64: rme: Allocate AUX RTT PGDs and VMIDs
   - 发件人: Steven Price <steven.price@arm.com>
6. **[09-26 12:02]** [RFC PATCH 5/5] arm64: RME: Support num_aux_places & rtt_tree_pp realm parameters
   - 发件人: Steven Price <steven.price@arm.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 updates for 6.18

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 25 Sep 2025 19:26:11 +0100

#### 🤖 AI 总结

本邮件讨论了 KVM/arm64 在 6.18 版本中的更新，主要由 Marc Zyngier 提交。此次更新包含多个修复和改进，尤其是针对 NV（非虚拟化）特性的后续支持和一些架构问题的解决。

在历史讨论中，没有提供具体的背景信息，但可以推测这次更新是对之前版本的一系列问题和特性的响应。

本周的讨论主要集中在以下几个方面的更新：
1. **FF-A 1.2 支持**：作为 pKVM 的安全内存通道，允许更多寄存器用于消息载荷。
2. **pKVM VM 句柄分配方式的改进**：确保特权虚拟机监控程序不会使用未初始化的数据。
3. **MMIO 范围注册的加速**：通过避免不必要的 RCU 同步，使虚拟机启动更快。
4. **EL2 中的指令流转储**：在 EL2 负载中发生崩溃时，能够转储指令流，有助于调试。
5. **52 位物理地址支持**：增强了页表遍历器的功能，以支持更大的地址空间。

此外，更新还包括多个修复和改进，旨在提升 KVM/arm64 的整体性能和稳定性。整体来看，这些更新为 KVM/arm64 的功能扩展和性能优化奠定了基础。

#### 📝 邮件列表

1. **[09-25 19:26]** [GIT PULL] KVM/arm64 updates for 6.18
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: KVM NV + SVE host OS warning

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 25 Sep 2025 15:38:14 +0100

#### 🤖 AI 总结

本邮件线程讨论了在 KVM 虚拟化环境中，使用 NV（Nested Virtualization）和 SVE（Scalable Vector Extension）时出现的主机操作系统警告问题。

**原始问题**：警告提示在有待处理异常时，程序计数器（PC）被递增，这被视为严重的错误。参与者 Jan Kotas 提出了这个问题，并寻求解决方案。

**之前讨论要点**：由于没有历史讨论，这里主要集中在本周的新讨论中。

**本周新讨论**：Marc Zyngier 提出了一个补丁建议，修改了 `sys_regs.c` 文件中的代码，以消除警告。他指出，虽然没有 NV+SVE 兼容的机器可供测试，但这个补丁应该能解决问题。Jan Kotas 表示他会尝试应用补丁，但由于没有相应的机器，更新内核可能会有挑战。Marc 进一步强调，使用命令行参数时要小心，并鼓励 Jan 测试补丁。Oliver Upton 也表示他在自己的测试环境中未能重现该错误，并认为补丁是合理的。

总体来看，讨论集中在寻找解决方案以消除警告，并强调了补丁的潜在有效性。

#### 📝 邮件列表

1. **[09-25 15:38]** Re: KVM NV + SVE host OS warning
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-25 15:10]** Re: KVM NV + SVE host OS warning
   - 发件人: Jan Kotas <jank@cadence.com>
3. **[09-25 16:35]** Re: KVM NV + SVE host OS warning
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-25 15:46]** Re: KVM NV + SVE host OS warning
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support

**📧 邮件数**: 11 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 25 Sep 2025 15:19:48 +0100

#### 🤖 AI 总结

本邮件讨论主题为“[kvm-unit-tests PATCH v3 00/10] arm64: EL2 support”，主要围绕在 EL2 环境下运行 kvm-unit-tests 的支持进行。Joey Gouly 提出了一个补丁系列，旨在增强对 EL2 的支持，并已在 Linux 6.17-rc6 KVM 嵌套虚拟化中进行测试。

在历史讨论中，补丁的核心内容是为 kvm-unit-tests 添加对 EL2 的支持，计划在未来扩展并添加新的嵌套虚拟化测试。补丁中提到了一些问题，如在 QEMU 和 kvmtool 下的调试测试失败，以及 gic ipi 测试在 QEMU 下超时但在 kvmtool 下正常工作。

本周的新讨论中，Joey 提交了多个补丁，涵盖了以下关键点：
1. **EL2 环境变量**：新增了一个环境变量，允许在启动时选择是否在 EL2 下运行。
2. **定时器和中断**：修复了在 EL2 下使用的定时器 IRQ，并确保在 EL2 下正确处理中断。
3. **异常级别初始化**：补丁确保在不支持 VHE 的情况下，能够从 EL2 降级到 EL1。
4. **微基准测试更新**：更新了微基准测试以支持在 EL2 下的执行，移除了对 EL1 的硬编码假设。

这些补丁的实施将为在 EL2 下的测试提供更好的支持，推动嵌套虚拟化的进一步发展。

#### 📝 邮件列表

1. **[09-25 15:19]** [kvm-unit-tests PATCH v3 00/10] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[09-25 15:19]** [kvm-unit-tests PATCH v3 01/10] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[09-25 15:19]** [kvm-unit-tests PATCH v3 02/10] arm64: efi: initialise SCTLR_ELx fully
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[09-25 15:19]** [kvm-unit-tests PATCH v3 03/10] arm64: efi: initialise the EL
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[09-25 15:19]** [kvm-unit-tests PATCH v3 04/10] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[09-25 15:19]** [kvm-unit-tests PATCH v3 05/10] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[09-25 15:19]** [kvm-unit-tests PATCH v3 06/10] arm64: micro-bench: use smc when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[09-25 15:19]** [kvm-unit-tests PATCH v3 07/10] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[09-25 15:19]** [kvm-unit-tests PATCH v3 08/10] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[09-25 15:19]** [kvm-unit-tests PATCH v3 09/10] arm64: run at EL2 if supported
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[09-25 15:19]** [kvm-unit-tests PATCH v3 10/10] arm64: add EL2 environment variable
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 2: [syzbot] Monthly kvmarm report (Sep 2025)

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 24 Sep 2025 05:39:35 -0700

#### 🤖 AI 总结

本周的邮件讨论主要是关于 kvmarm 子系统的月度报告，由 syzbot 提供。报告指出，在过去的 31 天内，检测到 3 个新问题，并修复了 1 个问题。目前仍有 4 个问题待解决，6 个问题已被修复。

具体来说，报告中列出了几个仍在发生的问题，包括：
1. **内核恐慌**：未处理的异常（Ref: 6087）
2. **KASAN**：在 `__kvm_pgtable_walk` 中的无效访问（Ref: 441）
3. **内核分页请求处理失败**：在 `vgic_its_save_tables_v0` 中（Ref: 10）

这些问题的详细信息可以通过提供的链接访问。报告强调了 kvmarm 子系统在稳定性方面仍面临的挑战，并为开发者提供了进一步调查和修复的方向。总体而言，本周的讨论没有涉及新的补丁或解决方案，而是集中在现有问题的跟踪和报告上。

#### 📝 邮件列表

1. **[09-24 05:39]** [syzbot] Monthly kvmarm report (Sep 2025)
   - 发件人: syzbot <syzbot+list12018f178486b71446df@syzkaller.appspotmail.com>

---

